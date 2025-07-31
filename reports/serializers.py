from rest_framework import serializers
from .models import SalesReport, ProductPerformance


class SalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReport
        fields = '__all__'

class ProductPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPerformance
        fields = '__all__'
