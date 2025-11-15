from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # redirect root to products list so http://127.0.0.1:8000/ shows the shop
    path('', RedirectView.as_view(url='/products/', permanent=False)),
    
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('products/', include('apps.products.urls')),
    path('orders/', include('apps.orders.urls')),
    path('cart/', include('apps.cart.urls')),
    path('checkout/', include('apps.payments.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)