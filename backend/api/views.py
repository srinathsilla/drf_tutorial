import json
from django.http import JsonResponse

# request is from HttpRequest - Django which is different from requests which is python requests library

def api_home(request):
    print(request.GET)  # url query parameters
    body = request.body     # byte string of json data
    data = {}
    try:
        data = json.loads(body) # string of json data -> python dict
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse(data)