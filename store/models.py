from django.db import models
from django.urls import reverse

from category.models import Category


# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length=100, unique=True)
    slug            = models.SlugField(max_length=100, unique=True)
    description     = models.TextField(blank=True, null=True)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    stock           = models.PositiveIntegerField(default=0)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_image   = models.ImageField(upload_to='photos/products', blank=True, null=True)
    is_available    = models.BooleanField(default=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    modified_at     = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def get_url(self):
        return reverse('product-detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name