from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description',
        'price', 'sale_start', 'sale_end')