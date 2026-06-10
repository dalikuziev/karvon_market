from django.db import models
from django_extensions.db.models import TimeStampedModel
from .category import Category

class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
