from django.urls import path
from .views import product_search

urlpatterns = [
    path('products/', product_search),  # /api/products/?query=...
]
