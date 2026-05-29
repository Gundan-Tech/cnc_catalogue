from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # This makes the products list show their name, price, and category in a nice table
    list_display = ('name', 'price', 'category', 'minimum_order')
    # This adds a filter sidebar on the right side of the admin page
    list_filter = ('category',)
    # This adds a search bar inside the admin dashboard
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)