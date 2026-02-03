# Import Django's admin module to register models in the admin interface
from django.contrib import admin
# Import all models from the current app to register them in admin
from .models import Category, Book, Customer, Order, OrderItem


# Register Category model with admin site and define its admin interface
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Define which fields to display in the category list view
    list_display = ['name', 'created_at']
    # Enable search functionality for the name field
    search_fields = ['name']


# Register Book model with admin site and define its admin interface
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Define which fields to display in the book list view
    list_display = ['title', 'author', 'isbn', 'category', 'price', 'stock', 'created_at']
    # Add filters for category and creation date in the sidebar
    list_filter = ['category', 'created_at']
    # Enable search functionality for title, author, and ISBN fields
    search_fields = ['title', 'author', 'isbn']
    # Allow inline editing of price and stock directly in the list view
    list_editable = ['price', 'stock']


# Register Customer model with admin site and define its admin interface
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # Define which fields to display in the customer list view
    list_display = ['user', 'phone', 'created_at']
    # Enable search functionality for username (via user relationship) and phone
    search_fields = ['user__username', 'phone']


# Define an inline admin interface for OrderItem to display within Order admin
class OrderItemInline(admin.TabularInline):
    # Specify the model to display inline
    model = OrderItem
    # Set number of empty forms to display (0 means no empty forms by default)
    extra = 0


# Register Order model with admin site and define its admin interface
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Define which fields to display in the order list view
    list_display = ['order_number', 'customer', 'status', 'total_amount', 'created_at']
    # Add filters for status and creation date in the sidebar
    list_filter = ['status', 'created_at']
    # Enable search functionality for order number and customer username
    search_fields = ['order_number', 'customer__user__username']
    # Include OrderItem inline forms within the Order admin page
    inlines = [OrderItemInline]