from rest_framework import mixins, viewsets

from products.serializers import ProductSerializer
from products.models import Product

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> QuerySet
    get -> retrieve -> Product Instance Detail View
    post -> create -> New insance
    put -> Update
    patch -> Partial Update
    delete -> destroy
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductGenericViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    get -> list -> QuerySet
    get -> retrieve -> Product Instance Detail View
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

product_list_view = ProductGenericViewset.as_view({'get':'list'})
product_detail_view = ProductGenericViewset.as_view({'get':'retrieve'})