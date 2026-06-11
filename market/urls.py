from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, ProductImageViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('product_image', ProductImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
