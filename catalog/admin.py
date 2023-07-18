from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'price', 'category', 'creation_date', 'last_change_date')
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)
