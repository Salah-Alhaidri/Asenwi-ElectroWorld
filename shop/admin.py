from django.contrib import admin
from django.utils.html import format_html  # Import this for rendering HTML safely
from shop.models import Category, Product

# Custom Admin Class for Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_dt')  # Fields to display in the list view
    search_fields = ('category_name',)  # Enable search by 'category_name'
    list_filter = ('created_dt',)  # Enable filtering by 'created_dt'
    ordering = ('-created_dt',)  # Default ordering

# Custom Admin Class for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_name', 'price', 'available_quantity', 'created', 'display_image')  # Add 'display_image'
    search_fields = ('name', 'category_name__category_name')  # Corrected to use 'category_name__category_name'
    list_filter = ('category_name', 'created')  # Enable filtering by 'category_name' and 'created'
    list_per_page = 20  # Number of items per page

    # Method to display the image in the admin
    def display_image(self, obj):
        if obj.prodect_image:  # Check if the image exists
            return format_html('<img src="{}" width="50" height="50" />', obj.prodect_image.url)
        return "No Image"
    
    display_image.short_description = 'Image'  # Column header name in the admin

# Register the models with their custom admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)