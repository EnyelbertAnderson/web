from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalesReportViewSet, ProductPerformanceViewSet

router = DefaultRouter()
router.register(r'sales-reports', SalesReportViewSet)
router.register(r'product-performance', ProductPerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
