import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = 'https://api.api-ninjas.com/v1/animals'
HEADERS = {
    "X-Api-Key": API_KEY
}


def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  response = requests.get(URL, headers=HEADERS, params=animal_name)
  if response.status_code == 200:
    data = response.json()
    return data
  else:
    print("data could not be retrieved")
    return None

