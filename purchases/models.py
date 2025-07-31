# purchases/models.py 
from django.db import models
from catalog.models import Supplier
from products.models import Product
from accounts.models import User
import uuid

class Purchase(models.Model):
    """Compras a proveedores"""
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('ordered', 'Ordenada'),
        ('received', 'Recibida'),
        ('cancelled', 'Cancelada'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    purchase_number = models.CharField(max_length=50, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='purchases')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Totales
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    # Fechas
    order_date = models.DateTimeField(auto_now_add=True)
    expected_date = models.DateTimeField(null=True, blank=True)
    received_date = models.DateTimeField(null=True, blank=True)
    
    # Usuario y documentos
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    invoice_number = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.purchase_number:
            from django.utils import timezone
            date_str = timezone.now().strftime('%Y%m%d')
            last_purchase = Purchase.objects.filter(purchase_number__startswith=f'COM-{date_str}').order_by('-purchase_number').first()
            if last_purchase:
                last_num = int(last_purchase.purchase_number.split('-')[-1])
                self.purchase_number = f'COM-{date_str}-{last_num + 1:04d}'
            else:
                self.purchase_number = f'COM-{date_str}-0001'
        super().save(*args, **kwargs)

class PurchaseItem(models.Model):
    """Items de compra"""
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity_ordered = models.PositiveIntegerField()
    quantity_received = models.PositiveIntegerField(default=0)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.total_cost = self.quantity_ordered * self.unit_cost
        super().save(*args, **kwargs)
