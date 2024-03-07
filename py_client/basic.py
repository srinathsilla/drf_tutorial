import requests

endpoint = "http://127.0.0.1:8001/api"

#get_response = requests.get(endpoint)   # HTTP Request
#get_response = requests.get(endpoint, json={"query":"Hello World!"})    # {'args': {}, 'data': '{"query": "Hello World!"}'..}
get_response = requests.get(endpoint, data={"query":"Hello World!"})    #{'args': {}, 'data': '', 'files': {}, 'form': {'query': 'Hello World!'} ..}


print(get_response.text)    # print raw text response

print(get_response.json())  # prints json data

print(get_response.status_code)