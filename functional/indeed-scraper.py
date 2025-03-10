import os
from dotenv import load_dotenv
import requests
import json
import logging

load_dotenv() 

def indeed_rapid_search(search_terms="information security analyst", location="San Francisco, CA", page="1"):
    try:
        url = "https://indeed12.p.rapidapi.com/jobs/search"

        payload = {
            "search_terms": search_terms,
            "location": location,
            "page": page
        }
        
        headers = {
            "x-rapidapi-key": os.getenv('X-RapidAPI-Key'), 
            "x-rapidapi-host": "X-RapidAPI-INDEED_Host",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Indeed RapidAPI error: {str(e)}")
        return None

if __name__ == "__main__":
    data = indeed_rapid_search()
    if data and isinstance(data, list):
        for item in data:
            print(json.dumps(item, indent=2))
		