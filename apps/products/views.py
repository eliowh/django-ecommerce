from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):
    # ?category=milk / ?category=yogurt / ?category=specials
    category_slug = request.GET.get('category')

    products = Product.objects.all()
    active_category = 'all'

    if category_slug:
        products = products.filter(category__slug=category_slug)
        active_category = category_slug

    context = {
        'products': products,
        'active_category': active_category,
    }
    return render(request, 'products/list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/detail.html', {'product': product})
