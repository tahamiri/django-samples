from django.urls import path
from .views import ProductListAPIView, ProductCreateView

urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name="product-list"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
]