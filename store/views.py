from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Product
from category.models import Category
from carts.views import _cart_id
from carts.models import CartItem

# Create your views here.

def store_home(request, category_slug=None):
    categories = None
    products = None


    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug,)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 6)  # Show 6 products per page if there are products
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 6)  # Show 6 products per page
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'title': 'Store Home',
        'product_count': product_count
    }
    return render(request, 'store/store_home.html', context)



def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug, is_available=True)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'title': single_product.product_name,
        'in_cart': in_cart
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_at').filter(product_name__icontains=keyword, is_available=True)
            product_count = products.count()
        else:
            products = Product.objects.none()
            product_count = 0
    else:
        products = Product.objects.none()
        product_count = 0

    context = {
        'products': products,
        'product_count': product_count,
        'title': 'Search Results'
    }
    return render(request, 'store/store_home.html', context)