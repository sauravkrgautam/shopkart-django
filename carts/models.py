from django.db import models

from store.models import Product, Variation

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=255, primary_key=True)
    # Using CharField for cart_id to allow for session keys or other identifiers
    # that may not be strictly numeric.
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.cart_id} - Added on {self.date_added.strftime('%Y-%m-%d %H:%M:%S')}"
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)


    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.product_name