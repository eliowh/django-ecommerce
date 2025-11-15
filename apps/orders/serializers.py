from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'  # or specify the fields you want to include, e.g., ['id', 'user', 'product', 'quantity', 'status']