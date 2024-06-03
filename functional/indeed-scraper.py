import os
from dotenv import load_dotenv
import requests
import json

load_dotenv() 

url = "https://indeed11.p.rapidapi.com/"

payload = {
	"search_terms": "information security analyst",
	"location": "San Francisco, CA",
	"page": "1"
}
headers = {
	"x-rapidapi-key": os.getenv('X_RapidAPI_Key'), 
	"x-rapidapi-host": "indeed11.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()

if isinstance(data, list):
    # Iterate over the list
    for item in data:
        # Pretty-print the item
        print(json.dumps(item, indent=4))