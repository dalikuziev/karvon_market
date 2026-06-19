from django.db import transaction
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, ProductImage, Category
from .serializers import ProductSerializer, ProductImageSerializer, CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        return Product.objects.all()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    @action(detail=True, methods=['post'])
    def sold(self, request, *args, **kwargs):
        product = self.get_object()
        with transaction.atomic():
            product.sold_count += 1
            product.save()
        return Response()
    @action(detail=False, methods=['get'])
    def top(self, request, *args, **kwargs):
        products = self.get_queryset().order_by('-sold_count')[:3]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Category.objects.all()

class ProductImageViewSet(viewsets.ModelViewSet):
    serializer_class = ProductImageSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return ProductImage.objects.all()
