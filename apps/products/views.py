from django.core.cache import cache
from rest_framework import generics
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer, ProductCreateSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_cache_key(self):
        category = self.request.query_params.get("category", "all")
        return f"product_list:category={category}"

    def list(self, request, *args, **kwargs):
        cache_key = self.get_cache_key()

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        queryset = Product.objects.filter(is_active=True)

        category = request.query_params.get("category")
        if category:
            queryset = queryset.filter(category=category)

        serializer = self.get_serializer(queryset, many=True)

        cache.set(cache_key, serializer.data, timeout=300)  # 5 min TTL

        return Response(serializer.data)
    
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer