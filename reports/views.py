
from rest_framework import viewsets
from .models import SalesReport, ProductPerformance
from .serializers import SalesReportSerializer, ProductPerformanceSerializer
from accounts.permissions import IsAdminOrSupervisor

class SalesReportViewSet(viewsets.ModelViewSet):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer
    permission_classes = [IsAdminOrSupervisor]

class ProductPerformanceViewSet(viewsets.ModelViewSet):
    queryset = ProductPerformance.objects.all()
    serializer_class = ProductPerformanceSerializer
    permission_classes = [IsAdminOrSupervisor]
