import requests
import os
from dotenv import load_dotenv

load_dotenv()

CITY = os.getenv("CITY")

url = f"https://geocoding-api.open-meteo.com/v1/search?name={CITY}&count=1&language=en&format=json"

response = requests.get(url)

data = response.json()

print(f"Status: {response.status_code}")
print(data)