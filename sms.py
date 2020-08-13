import os
import africastalking
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USERNAME')
api_key = os.getenv('API_KEY')

africastalking.initialize(username, api_key)

sms = africastalking.SMS

response = sms.send('I can do anything that I set my mind to', ['+256783449059'])

print(response)
