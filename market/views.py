from rest_framework import viewsets, serializers
from .models import Product, ProductImage, Category
from .serializers import ProductSerializer, ProductImageSerializer, CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # def validate_name(self, value):
    #     if not value.startswith('a'):
    #         raise serializers.ValidationError(detail="bunaqa boshlama")
    #     return value

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
