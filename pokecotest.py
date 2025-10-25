import requests

API_KEY = 'pk_nY_0FmfBPNCDd7xNPnzcIb4rNKmuaqg2x5kgouA2raE'
MESSAGE = 'Hello from Cal Hacks!'

response = requests.post(
    'https://poke.com/api/v1/inbound-sms/webhook',
    headers={
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    },
    json={'message': MESSAGE}
)

print(response.json())