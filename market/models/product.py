from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.conf import settings

class Product(TimeStampedModel):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products',
    )
    category = models.ForeignKey(
        'market.Category',
        on_delete=models.CASCADE,
        related_name='products',
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
