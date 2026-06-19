from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, ProductImageViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('category', CategoryViewSet, basename='category')
router.register('product_image', ProductImageViewSet, basename='product_image')

urlpatterns = [
    path('', include(router.urls)),
]
