# Import Django's models module and built-in User model
from django.db import models
from django.contrib.auth.models import User

# Model for book categories 
class Category(models.Model):
    # Fields: name, description, created timestamp
    name = models.CharField(max_length=100, verbose_name="Category Name")
    description = models.TextField(blank=True, verbose_name="Category Description")
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Meta options for admin display
    class Meta:
        verbose_name = "Book Category"
        verbose_name_plural = "Book Categories"
    
    def __str__(self):
        return self.name


# Model for individual books with details like title, author, price, stock
class Book(models.Model):
    """Book information"""
    # Basic book fields: title, author, ISBN, category, price, stock
    title = models.CharField(max_length=200, verbose_name="Book Name")
    author = models.CharField(max_length=100, verbose_name="Author")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books', verbose_name="Category")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    stock = models.IntegerField(default=0, verbose_name="Stock")
    # Additional optional fields: description, publisher, dates, cover image
    description = models.TextField(blank=True, verbose_name="Description")
    publisher = models.CharField(max_length=100, blank=True, verbose_name="Publisher")
    publish_date = models.DateField(null=True, blank=True, verbose_name="Publish Date")
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name="Cover Image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Meta options: display names and ordering (newest first)
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


# Model for customer profile extending Django's User model
class Customer(models.Model):
    """Customer information"""
    # Gender choices for dropdown
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    # Customer fields: user link, personal info (age, gender, contact), premium status
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    age = models.IntegerField(null=True, blank=True, verbose_name="Age")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, verbose_name="Gender")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Phone")
    address = models.TextField(blank=True, verbose_name="Address")
    email = models.EmailField(max_length=254, blank=True, verbose_name="Email")
    is_premium = models.BooleanField(default=False, verbose_name="Premium Member")
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Meta options for admin display
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
    
    def __str__(self):
        return f"{self.user.username} - Customer"


# Model for customer orders with status tracking
class Order(models.Model):
    """Order"""
    # Order status choices (pending, confirmed, shipped, delivered, cancelled)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    # Order fields: customer, order number, status, total, address, timestamps
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', verbose_name="Customer")
    order_number = models.CharField(max_length=50, unique=True, verbose_name="Order Number")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Status")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Amount")
    shipping_address = models.TextField(verbose_name="Shipping Address")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Order Created At")
    updated_at = models.DateTimeField(auto_now=True)
    
    # Meta options: display names and ordering (newest first)
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Order {self.order_number}"


# Model for individual items in an order (junction table between Order and Book)
class OrderItem(models.Model):
    """Order items"""
    # OrderItem fields: order link, book link, quantity, price at time of purchase
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="Order")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Book")
    quantity = models.IntegerField(default=1, verbose_name="Quantity")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    
    # Meta options for admin display
    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
    
    def __str__(self):
        return f"{self.book.title} x {self.quantity}"
    
    # Calculate subtotal for this item (quantity × price)
    def get_subtotal(self):
        return self.quantity * self.price
