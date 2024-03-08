import requests

endpoint = "http://127.0.0.1:8001/api/products/1/update/"

data = {
    "title": "Hello World my old friend",
    "price": 129.99
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())