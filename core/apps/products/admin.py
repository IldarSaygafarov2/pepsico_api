from django.contrib import admin

from .models import Product, ProductSize


class ProductSizeInline(admin.StackedInline):
    model = ProductSize
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline]
