from django.contrib import admin

from django.contrib import admin
from .models import Product  # Import the Product model

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Customize how the Product model appears in the admin interface
    list_display = ('name', 'price', 'created_at')  # Fields to display in the list view
    search_fields = ('name', 'description')  # Fields to include in the search box
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate the slug based on the name

