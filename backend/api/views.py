from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

# request is from HttpRequest - Django which is different from requests which is python requests library

@api_view(['GET'])
def api_home(request):
    '''
    DRF API view
    '''
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
        # data = model_to_dict(instance, fields = ['id', 'title', 'price', 'sale_price'])
    return Response(data)