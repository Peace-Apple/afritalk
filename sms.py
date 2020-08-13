import os
import africastalking
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USERNAME')
api_key = os.getenv('API_KEY')

africastalking.initialize(username, api_key)

sms = africastalking.SMS

message = 'I can do anything that I set my mind to'

receipients = ['+256796895642']

response = sms.send(message, receipients)

print(response)
