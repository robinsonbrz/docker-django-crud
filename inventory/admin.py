from django.contrib import admin

# Register your models here.
from .models import Product, Brand, Category, Stock

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Stock)