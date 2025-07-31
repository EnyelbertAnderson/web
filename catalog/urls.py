from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubcategoryViewSet, BrandViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'brands', BrandViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
