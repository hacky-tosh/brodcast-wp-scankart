import os
from twilio.rest import Client

account_sid = "ACbdc168dca911102b852f87bd8f5c7138"
auth_token = "0432f9e8fd93aad30638868b9bc101eb"
client = Client(account_sid, auth_token)




def send_bulk_sms_wp(body,numbers):
    result = []
    for num in numbers:
        num = int(num[-10:])
        message = client.messages.create(
            body=body,
            from_='whatsapp:+916901261956',
            to=f'whatsapp:+91{int(num)}'
        )
        print("-------------")
        print(message)
        print(message.sid)
        print(message.status)
        print("-------------")
        result.append(result)
    
    return result


