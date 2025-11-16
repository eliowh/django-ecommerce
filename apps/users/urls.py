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

    # login/logout using Django’s built-in views
    # /users/login/
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'
    ), name='login'),

    # /users/logout/
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]