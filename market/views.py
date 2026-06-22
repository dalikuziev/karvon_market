from django.db import transaction
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, ProductImage, Category
from .serializers import ProductSerializer, ProductImageSerializer, CategorySerializer
from django.db.models import F
from django.contrib.postgres.search import TrigramSimilarity

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = Product.objects.filter(owner=self.request.user)
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.annotate(
                name_similarity=TrigramSimilarity('name', search),
                desc_similarity=TrigramSimilarity('description', search)
            ).annotate(
                similarity=F("name_similarity") + F("desc_similarity"),
            ).filter(
                similarity__gt=0.3
            ).order_by('-similarity')

        return queryset

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
