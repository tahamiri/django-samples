from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from .models import Product


CACHE_PATTERN = "product_list:*"


def clear_product_cache():
    cache.delete_pattern(CACHE_PATTERN)


@receiver(post_save, sender=Product)
def product_saved(sender, instance, **kwargs):
    clear_product_cache()


@receiver(post_delete, sender=Product)
def product_deleted(sender, instance, **kwargs):
    clear_product_cache()