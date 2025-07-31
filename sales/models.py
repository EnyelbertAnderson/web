# sales/models.py 
from django.db import models
from products.models import Product
from accounts.models import User
import uuid

class Customer(models.Model):
    """Clientes"""
    CUSTOMER_TYPES = [
        ('individual', 'Persona Natural'),
        ('business', 'Empresa'),
        ('reseller', 'Revendedor'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPES, default='individual')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    company_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    tax_id = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def full_name(self):
        if self.customer_type == 'business':
            return self.company_name
        return f"{self.first_name} {self.last_name}".strip()

class Sale(models.Model):
    """Ventas principales"""
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmada'),
        ('shipped', 'Enviada'),
        ('delivered', 'Entregada'),
        ('cancelled', 'Cancelada'),
        ('returned', 'Devuelta'),
    ]
    
    PAYMENT_METHODS = [
        ('cash', 'Efectivo'),
        ('card', 'Tarjeta'),
        ('transfer', 'Transferencia'),
        ('credit', 'Crédito'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='sales')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    
    # Totales
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    # Fechas
    sale_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    
    # Usuario y notas
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='sales_created')
    notes = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.sale_number:
            # Generar número de venta automático
            from django.utils import timezone
            date_str = timezone.now().strftime('%Y%m%d')
            last_sale = Sale.objects.filter(sale_number__startswith=f'VTA-{date_str}').order_by('-sale_number').first()
            if last_sale:
                last_num = int(last_sale.sale_number.split('-')[-1])
                self.sale_number = f'VTA-{date_str}-{last_num + 1:04d}'
            else:
                self.sale_number = f'VTA-{date_str}-0001'
        super().save(*args, **kwargs)

class SaleItem(models.Model):
    """Items de venta"""
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        self.discount_amount = (self.subtotal * self.discount_percentage) / 100
        self.total = self.subtotal - self.discount_amount
        super().save(*args, **kwargs)

