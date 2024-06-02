import os
from dotenv import load_dotenv
import requests

load_dotenv()  # load environment variables from .env file

url = "https://rapid-linkedin-jobs-api.p.rapidapi.com/search-jobs-v2"

querystring = {"keywords":"information security analyst","locationId":"92000000","datePosted":"pastWeek","salary":"90k+","experienceLevel":"midSeniorLevel","sort":"mostRelevant"}

headers = {
    "x-rapidapi-key": os.getenv('X_RapidAPI_Key'), 
    "x-rapidapi-host": "rapid-linkedin-jobs-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())