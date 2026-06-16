from django.db import models
from django.conf import settings
from django.contrib.postgres.indexes import HashIndex
from apps.core.models import TimeStampedModel


class Order(TimeStampedModel):

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        SHIPPED = "shipped", "Shipped"
        DELIVERED = "delivered", "Delivered"
        CANCELLED = "cancelled", "Cancelled"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="orders",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            HashIndex(fields=['status'], name='status_hash_idx'),
            models.Index(fields=['user']),
        ]

    def __str__(self):
        return f"Order {self.pk} — {self.user} — {self.status}"


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.PROTECT,
        related_name="order_items",
    )
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['product']),
            models.Index(fields=['order']),
        ]

    def __str__(self):
        return f"{self.quantity}x {self.product} (Order {self.order_id})"

    @property
    def subtotal(self):
        return self.quantity * self.unit_price