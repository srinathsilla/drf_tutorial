import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from products.models import Product

# request is from HttpRequest - Django which is different from requests which is python requests library

def api_home(request):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields = ['id', 'title', 'price'])

    return JsonResponse(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type":"application/json"})