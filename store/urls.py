from django.urls import path
from . import views 

urlpatterns = [
    # Define your URL patterns here
    path('', views.store_home, name='store-home'),
    path('<slug:category_slug>/', views.store_home, name='store-category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product-detail'),
]