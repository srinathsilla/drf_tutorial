import requests

# always make sure to end url with trailing slash when sending params and request data over get request,
endpoint = "http://127.0.0.1:8001/api/"

#get_response = requests.get(endpoint)   # HTTP Request
#get_response = requests.get(endpoint, json={"query":"Hello World!"})    # {'args': {}, 'data': '{"query": "Hello World!"}'..}
#get_response = requests.get(endpoint, data={"query":"Hello World!"})    #{'args': {}, 'data': '', 'files': {}, 'form': {'query': 'Hello World!'} ..}

get_response = requests.get(endpoint, params={"abc":123}, json={"query":"Hello World"})

#print(get_response.text)    # print raw text response

print(get_response.json())  # prints json data

#print(get_response.status_code)


# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# Javascript object Notation ~ Python Dict