import requests

endpoint = "http://127.0.0.1:8001/api/products/7/"

get_response = requests.get(endpoint)

print(get_response.json())