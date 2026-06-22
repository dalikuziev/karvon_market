from rest_framework import serializers
from .models import Product, Category, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'description', 'price', 'sold_count')

class ProductImageSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'image')
    def validate_image(self, value):
        if not len(value) > 12:
            raise serializers.ValidationError("sal uzunroq url ber")
        return value
