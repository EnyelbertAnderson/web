# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, ProductSpecification, ProductImage
from .serializers import ProductSerializer, ProductSpecificationSerializer, ProductImageSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductSpecificationViewSet(viewsets.ModelViewSet):
    queryset = ProductSpecification.objects.all()
    serializer_class = ProductSpecificationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
