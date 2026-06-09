from django.db import models
from django_extensions.db.models import TimeStampedModel
from .product import Product

class ProductImage(TimeStampedModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(upload_to="products/")
