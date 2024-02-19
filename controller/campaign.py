from flask import jsonify
from flask import request
from datetime import datetime, timedelta
from dotenv import load_dotenv
from utilities import sms
import os
import threading
import time

load_dotenv()
from config.firebase_config import db 

users_collection = db.collection('wpuser')

def send_bulk_sms():
    try:
        data = request.get_json()
        print(data)
        numbers = data.get('numbers')
        campaign_name = data.get('name')
        body = data.get('message')
        user_email = data.get('email')
        

        
        sms_data = {
            "campaign_name":campaign_name,
              'body':body,
             "numbers":numbers
        }
        
        print(sms_data)
        
        user_doc = users_collection.where('email','==',user_email).get()
        
        if not user_doc:
            return jsonify({'message':'User not found'}),400
        
        sms_thread = threading.Thread(target=sms.send_bulk_sms_wp, args=(body, numbers))
        sms_thread.start()
        
        user_id = user_doc[0].id
        campaign_collection = users_collection.document(user_id).collection('campaign')
        campaign_collection.add(sms_data)
        
        return jsonify({'message':'sms sent successfully'}),200
        
        
        
    
    except Exception as e:
        return jsonify({'message':'sms not sent'}),400
    