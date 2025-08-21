from django.contrib import admin

# Register your models here.

from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')
    search_fields = ('cart_id',)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')
    list_filter = ('cart', 'is_active')
    search_fields = ('product__product_name', 'cart__cart_id')

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)