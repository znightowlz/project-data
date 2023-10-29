from django.contrib import admin
from app_products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'amount', 'image_relative_url']


# Register your models here.
admin.site.register(Product, ProductAdmin)