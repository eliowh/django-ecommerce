from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from .serializers import OrderSerializer
from rest_framework import viewsets

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        orders = self.get_queryset()
        serializer = self.get_serializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, *args, **kwargs):
        order = self.get_object()
        serializer = self.get_serializer(order)
        return JsonResponse(serializer.data)