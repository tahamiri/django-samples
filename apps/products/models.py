from django.db import models
from django.contrib.postgres.indexes import HashIndex
from apps.core.models import TimeStampedModel


class Product(TimeStampedModel):

    class Category(models.TextChoices):
        ELECTRONICS = "electronics", "Electronics"
        CLOTHING = "clothing", "Clothing"
        FOOD = "food", "Food"
        BOOKS = "books", "Books"
        OTHER = "other", "Other"

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=50,
        choices=Category.choices,
        default=Category.OTHER,
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            HashIndex(fields=['category'], name='category_hash_idx'),
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name