from django.urls import path
from . import views

# Namespace so templates can use {% url 'products:list' %}
app_name = 'products'

urlpatterns = [
    # /products/
    path('', views.product_list, name='list'),

    # /products/1/
    path('<int:pk>/', views.product_detail, name='detail'),
]