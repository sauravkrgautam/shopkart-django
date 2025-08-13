from django.contrib import admin

from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'stock', 'modified_at','is_available')
    list_display_links = ('product_name',)
    prepopulated_fields = {'slug': ('product_name',)}
    search_fields = ('product_name', 'category__category_name')
    list_filter = ('category', 'is_available', 'price')

admin.site.register(Product, ProductAdmin) 
