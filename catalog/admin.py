from django.contrib import admin

from catalog.models import Product, Category, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'price', 'category', 'creation_date', 'last_change_date')
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'version_number', 'version_name', 'version_sing')
    list_filter = ('version_sing',)
    search_fields = ('product', 'version_name',)
