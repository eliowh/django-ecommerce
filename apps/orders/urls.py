from django.urls import path
from . import views

# The app uses a DRF ViewSet (OrderViewSet). Map the common endpoints to the viewset actions.
order_list = views.OrderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
order_detail = views.OrderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('orders/', order_list, name='order-list'),
    path('orders/<int:pk>/', order_detail, name='order-detail'),
]