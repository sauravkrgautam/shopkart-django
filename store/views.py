from django.shortcuts import render, get_object_or_404

from .models import Product
from category.models import Category

# Create your views here.

def store_home(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug,)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'title': 'Store Home',
        'product_count': product_count
    }
    return render(request, 'store/store_home.html', context)



def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug, is_available=True)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'title': single_product.product_name
    }
    return render(request, 'store/product_detail.html', context)