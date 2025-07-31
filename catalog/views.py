
from rest_framework import viewsets
from .models import Category, Subcategory, Brand
from .serializers import CategorySerializer, SubcategorySerializer, BrandSerializer
from .permissions import IsAdminOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminOrReadOnly]
