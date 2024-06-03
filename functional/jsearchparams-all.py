import os
from dotenv import load_dotenv
import requests

load_dotenv() 

url = "https://jsearch.p.rapidapi.com/search"

querystring = {"query":"information security analyst in San Francisco USA","page":"1","num_pages":"1","date_posted":"week","employment_types":"FULLTIME","actively_hiring":"true","radius":"15"}

headers = {
	"x-rapidapi-key": os.getenv('X_RapidAPI_Key'), 
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())