from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from apps.cart.views import merge_session_cart_to_user_cart

def register(request):
    if request.method == 'POST':
        # Use the custom form with email field
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Merge session cart with new user's cart
            merge_session_cart_to_user_cart(request, user)
            messages.success(request, f'Account created successfully for {user.username}!')
            return redirect('products:list')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def custom_login(request):
    """Custom login view that merges session cart with user cart"""
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Merge session cart with user cart
                merge_session_cart_to_user_cart(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('products:list')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please fill in all required fields.')
    else:
        form = UserLoginForm()
    
    return render(request, 'users/login.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')