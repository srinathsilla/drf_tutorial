import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

#get_response = requests.get(endpoint)   # HTTP Request
#get_response = requests.get(endpoint, json={"query":"Hello World!"})    # {'args': {}, 'data': '{"query": "Hello World!"}'..}
get_response = requests.get(endpoint, data={"query":"Hello World!"})    #{'args': {}, 'data': '', 'files': {}, 'form': {'query': 'Hello World!'} ..}


#print(get_response.text)    # print raw text response

print(get_response.json())  # prints json data

print(get_response.status_code)