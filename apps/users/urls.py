from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# namespace so templates can use {% url 'users:login' %}
app_name = 'users'

urlpatterns = [
    # /users/register/
    path('register/', views.register, name='register'),

    # /users/profile/
    path('profile/', views.profile, name='profile'),

    # login/logout using custom and built-in views
    # /users/login/
    path('login/', views.custom_login, name='login'),

    # /users/logout/
    path('logout/', auth_views.LogoutView.as_view(next_page='users:login'), name='logout'),
]