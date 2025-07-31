
from rest_framework import viewsets
from .models import Sale
from .serializers import SaleSerializer
from accounts.permissions import IsAdminOrSeller

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAdminOrSeller]
