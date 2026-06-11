from django.db import models
from django_extensions.db.models import TimeStampedModel
class ProductImage(TimeStampedModel):
    product = models.ForeignKey(
        'market.Product',
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.URLField()
