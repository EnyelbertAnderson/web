# catalog/models.py 
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    """Categorías principales de componentes electrónicos"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    """Subcategorías específicas"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Subcategories"
        unique_together = ['category', 'name']
        ordering = ['category', 'name']
    
    def __str__(self):
        return f"{self.category.name} > {self.name}"

class Brand(models.Model):
    """Marcas de componentes"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Supplier(models.Model):
    """Proveedores"""
    name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    tax_id = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=2, 
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
