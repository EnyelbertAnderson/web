# inventory/models.py 
from django.db import models
from products.models import Product
from accounts.models import User
import uuid

class Stock(models.Model):
    """Control de inventario por producto"""
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='stock')
    current_quantity = models.PositiveIntegerField(default=0)
    reserved_quantity = models.PositiveIntegerField(default=0)  # Para órdenes pendientes
    available_quantity = models.PositiveIntegerField(default=0)
    last_restock_date = models.DateTimeField(null=True, blank=True)
    last_sale_date = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def is_low_stock(self):
        return self.available_quantity <= self.product.reorder_point
    
    @property
    def is_out_of_stock(self):
        return self.available_quantity == 0
    
    def save(self, *args, **kwargs):
        self.available_quantity = max(0, self.current_quantity - self.reserved_quantity)
        super().save(*args, **kwargs)

class StockMovement(models.Model):
    """Historial de movimientos de inventario"""
    MOVEMENT_TYPES = [
        ('purchase', 'Compra'),
        ('sale', 'Venta'),
        ('adjustment', 'Ajuste'),
        ('return', 'Devolución'),
        ('damaged', 'Dañado'),
        ('transfer', 'Transferencia'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_movements')
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPES)
    quantity = models.IntegerField()  # Puede ser negativo para salidas
    previous_quantity = models.PositiveIntegerField()
    new_quantity = models.PositiveIntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    reference_document = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

