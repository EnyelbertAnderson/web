
from rest_framework import viewsets
from .models import Stock
from .serializers import StockSerializer
from accounts.permissions import IsAdminOrSupervisor

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdminOrSupervisor]
