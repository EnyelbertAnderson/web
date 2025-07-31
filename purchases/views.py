
from rest_framework import viewsets
from .models import Purchase
from .serializers import PurchaseSerializer
from accounts.permissions import IsAdminOrSupervisor

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAdminOrSupervisor]
