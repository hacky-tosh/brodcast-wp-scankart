from flask import jsonify
from flask import request
from datetime import datetime
# from dotenv import load_dotenv
# load_dotenv()
from config.firebase_config import db  # Assuming this is correctly configured
import pandas as pd

users_collection = db.collection('wpuser')


def get_all_contacts():
    try:
        # data = request.get_json()
        user_email = request.args.get('email')
        print(user_email)
        user_doc = users_collection.where('email', '==', user_email).get()
        if not user_doc:
            return jsonify({'message': 'User not found'}), 400
        user_id = user_doc[0].id
        wpcontacts_ref = users_collection.document(user_id).collection('wpcontacts')
        docs = wpcontacts_ref.stream()
        contacts = []
        for doc in docs:
            contact = doc.to_dict()
            contact['id'] = doc.id
            contacts.append(contact)
        return jsonify(contacts), 200
    except:
        return jsonify({'message': 'Contacts not found'}), 400



def upload_contacts():
    try:
        
        excel_file = request.files['file']
        df = pd.read_excel(excel_file)
        user_email = request.form.get('user_email')

        for index, row in df.iterrows():
            name = row['Name']
            number = row['Number']
            source = 'Excel'
            date_added = datetime.now()

            contact_data = {
                'name': name,
                'number': number,
                'source': source,
                'date_added': date_added,
            }

            user_doc = users_collection.where('email', '==', user_email).get()

            if not user_doc:
                return jsonify({'message': 'User not found'}), 400

            user_id = user_doc[0].id

            wpcontacts_ref = users_collection.document(user_id).collection('wpcontacts')
            wpcontacts_ref.add(contact_data)

        return jsonify({'message': 'Contacts uploaded successfully'}), 201
    except Exception as e:
        print(str(e))  # Print or log the specific error message
        return jsonify({'message': 'Contacts not uploaded'}), 400


def add_single_contact():
    try:
        data = request.get_json()
        print(data)
        name = data.get('name')
        number = data.get('number')
        source = 'Direct'
        date_added = datetime.now()
        user_email = data.get('user_email')
        
        contact_data = {
            'name': name,
            'number': number,
            'source': source,
            'date_added': date_added,
        }
        
        user_doc = users_collection.where('email', '==', user_email).get()
        
        user_id = user_doc[0].id

        wpcontacts_ref = users_collection.document(user_id).collection('wpcontacts')
        wpcontacts_ref.add(contact_data)
        
        return jsonify({'message': 'Contact added successfully'}), 201
    except:
        return jsonify({'message': 'Contact not added'}), 400
    
