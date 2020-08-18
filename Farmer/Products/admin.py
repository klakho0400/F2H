from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('seller', 'name', 'price', 'stock')


admin.site.register(Product, ProductAdmin)
