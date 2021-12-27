from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer
from .models import Product

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
