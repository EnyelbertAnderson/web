from rest_framework import serializers
from .models import Product, ProductSpecification, ProductImage

class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = ['id', 'spec_name', 'spec_value', 'unit', 'is_critical']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text', 'is_primary', 'order']

class ProductSerializer(serializers.ModelSerializer):
    specifications = ProductSpecificationSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = [
            'id', 'sku', 'name', 'description',
            'category', 'subcategory', 'brand',
            'model_number', 'part_number', 'datasheet_url',
            'package_type', 'dimensions', 'weight',
            'cost_price', 'selling_price', 'margin_percentage',
            'min_stock', 'max_stock', 'reorder_point',
            'is_active', 'is_featured',
            'created_by', 'created_at', 'updated_at',
            'specifications', 'images',
        ]
