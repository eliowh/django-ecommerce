from django.urls import path
from . import views

order_list = views.OrderViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

order_detail = views.OrderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    # /orders/
    path('', order_list, name='order_list'),

    # /orders/1/
    path('<int:pk>/', order_detail, name='order-detail'),
]