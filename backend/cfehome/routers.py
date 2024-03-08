from products.viewsets import ProductViewSet, ProductGenericViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductGenericViewset, basename='products')
print(router.urls)
urlpatterns = router.urls