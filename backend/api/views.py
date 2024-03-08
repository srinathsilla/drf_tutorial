from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from products.models import Product
from products.serializers import ProductSerializer

# request is from HttpRequest - Django which is different from requests which is python requests library

@api_view(['POST'])
def api_home(request):
    '''
    DRF API view
    '''
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        #instance = serializer.save()
        # similar to instance  form.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid":"Not good data"}, status=400)