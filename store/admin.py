from django.contrib import admin

from .models import Product, Variation
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'stock', 'modified_at','is_available')
    list_display_links = ('product_name',)
    prepopulated_fields = {'slug': ('product_name',)}
    search_fields = ('product_name', 'category__category_name')
    list_filter = ('category', 'is_available', 'price')

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_filter = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('product__product_name', 'variation_value')

admin.site.register(Product, ProductAdmin) 
admin.site.register(Variation, VariationAdmin)
