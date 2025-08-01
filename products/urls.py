from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductSpecificationViewSet, ProductImageViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'product-specs', ProductSpecificationViewSet)
router.register(r'product-images', ProductImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
