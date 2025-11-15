from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# namespace so templates can use {% url 'users:login' %}
app_name = 'users'

urlpatterns = [
    # register/profile use the function-based views defined in apps/users/views.py
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # use Django's built-in auth views for login/logout (templates can be customized)
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]