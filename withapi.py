import requests

API_KEY = '+PxEWWsrKKPRfoyCyksXZg==0BlJ1b7TgKADjCWc'
URL = 'https://api.api-ninjas.com/v1/animals'
HEADERS = {
    "X-Api-Key": API_KEY
}

params = {"name": "dog"}  # Replace "dog" with the desired animal
response = requests.get(URL, headers=HEADERS, params=params)

print (response.status_code)

if response.status_code == 200:
    data = response.json()
    print(data)
