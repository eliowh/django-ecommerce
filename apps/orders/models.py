from django.db import models
from apps.users.models import User
from apps.products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"Address for Order {self.order.id}"