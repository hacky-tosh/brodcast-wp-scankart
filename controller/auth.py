# auth.py

from flask import jsonify
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import jwt
from dotenv import load_dotenv
import os
load_dotenv()
from config.firebase_config import db 

users_collection = db.collection('wpuser')


def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name  = data.get('name')

    # Check if email already exists
    if users_collection.where('email', '==', email).get():
        return jsonify({'message': 'Email already exists'}), 400

    # Hash the password
    hashed_password = generate_password_hash(password, method='sha256')

    # Save user to Firebase
    user_data = {
        'name': name,
        'email': email,
        'password': hashed_password
    }
    users_collection.add(user_data)

    return jsonify({'message': 'Signup successful'}), 201


def login():

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    print(email, password)

    # Check if email exists
    user_query = users_collection.where('email', '==', email).get()
    print(user_query)
    if not user_query:
        return jsonify({'message': 'Invalid email or password'}), 401

    # Verify password
    user_data = user_query[0].to_dict()
    if not check_password_hash(user_data['password'], password):
        return jsonify({'message': 'Invalid email or password'}), 401

    # Set expiration time to 1 hour from now
    expiration_time = datetime.utcnow() + timedelta(hours=1)

    # Generate JWT token with expiration time
    token = jwt.encode({'email': email, 'exp': expiration_time}, os.getenv('SECRET_KEY'), algorithm='HS256')

    # Include email in the JSON response
    response_data = {
        'email': email,
        'token': token.decode('utf-8'),
        'expiration_time': expiration_time.strftime('%Y-%m-%d %H:%M:%S')
    }

    return jsonify(response_data), 200
