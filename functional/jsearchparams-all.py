import requests

url = "https://jsearch.p.rapidapi.com/search"

querystring = {"query":"information security analyst in San Francisco USA","page":"1","num_pages":"1","date_posted":"week","employment_types":"FULLTIME","actively_hiring":"true","radius":"15"}

headers = {
	"x-rapidapi-key": "398a4b4962mshd8284c9a0ccbcb9p1f24fcjsn457f5a0c7d3a",
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())