# reports/models.py 
from django.db import models
from products.models import Product

class SalesReport(models.Model):
    """Vista materializada para reportes de ventas"""
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_transactions = models.PositiveIntegerField(default=0)
    top_selling_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    average_transaction = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['date']
        ordering = ['-date']

class ProductPerformance(models.Model):
    """Rendimiento de productos"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    period_start = models.DateField()
    period_end = models.DateField()
    units_sold = models.PositiveIntegerField(default=0)
    revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    profit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    margin_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    ranking = models.PositiveIntegerField(null=True, blank=True)
    
    class Meta:
        unique_together = ['product', 'period_start', 'period_end']
        ordering = ['-revenue']
