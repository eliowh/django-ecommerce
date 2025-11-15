from django.urls import path
from . import views

# Namespace for reverse lookups from templates like {% url 'products:list' %}
app_name = 'products'

urlpatterns = [
    # keep simple names 'list' and 'detail' so templates can use products:list / products:detail
    path('', views.product_list, name='list'),
    path('<int:pk>/', views.product_detail, name='detail'),
]