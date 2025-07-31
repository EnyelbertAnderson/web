# products/models.py 
from django.db import models
from catalog.models import Category, Subcategory, Brand
from accounts.models import User
import uuid

class Product(models.Model):
    """Producto principal - Componente electrónico"""
    # Identificación básica
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    # Clasificación
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    
    # Especificaciones técnicas (campos comunes para electrónicos)
    model_number = models.CharField(max_length=100, blank=True)
    part_number = models.CharField(max_length=100, blank=True)
    datasheet_url = models.URLField(blank=True)
    
    # Características físicas
    package_type = models.CharField(max_length=50, blank=True)  # DIP, SMD, etc.
    dimensions = models.CharField(max_length=100, blank=True)  # mm
    weight = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)  # gramos
    
    # Precios
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    margin_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    # Inventario
    min_stock = models.PositiveIntegerField(default=10)
    max_stock = models.PositiveIntegerField(default=1000)
    reorder_point = models.PositiveIntegerField(default=20)
    
    # Estado
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    
    # Metadatos
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='products_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # Calcular margen automáticamente
        if self.cost_price and self.selling_price:
            self.margin_percentage = ((self.selling_price - self.cost_price) / self.cost_price) * 100
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.sku} - {self.name}"

class ProductSpecification(models.Model):
    """Especificaciones técnicas específicas por producto"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    spec_name = models.CharField(max_length=100)  # Voltaje, Corriente, Frecuencia, etc.
    spec_value = models.CharField(max_length=200)
    unit = models.CharField(max_length=20, blank=True)  # V, A, Hz, etc.
    is_critical = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['product', 'spec_name']
    
    def __str__(self):
        return f"{self.product.name} - {self.spec_name}: {self.spec_value} {self.unit}"

class ProductImage(models.Model):
    """Imágenes de productos"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images/')
    alt_text = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'id']

