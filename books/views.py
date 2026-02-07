# Import path for URL routing and views from current app
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from decimal import Decimal
from datetime import datetime

# Import your models
# Import Book, Category, Customer, Order, and OrderItem models from the current app
from .models import Book, Category, Customer, Order, OrderItem


# Define the index view function that takes a request object
def index(request):
    # Docstring describing this view as the homepage
    """Homepage"""
    # Query the database to get the first 12 books
    books = Book.objects.all()[:12]
    # Query the database to get all categories
    categories = Category.objects.all()
    # Create a context dictionary to pass data to the template
    context = {
        # Add books to the context
        'books': books,
        # Add categories to the context
        'categories': categories,
    }
    # Render the index.html template with the context data and return the response
    return render(request, 'index.html', context) 


# Define the book_list view function
def book_list(request):
    # Docstring describing this view as the book list
    """Book list"""
    # Query the database to get all books
    books = Book.objects.all()
    # Get the category filter parameter from the URL query string
    category_id = request.GET.get('category')
    # Get the search query parameter from the URL query string
    search_query = request.GET.get('search')
    
    # Check if a category filter was provided
    if category_id:
        # Filter books by the selected category
        books = books.filter(category_id=category_id)
    
    # Check if a search query was provided
    if search_query:
        # Filter books by title, author, or ISBN containing the search query
        books = books.filter(
            # Search in title field (case-insensitive)
            Q(title__icontains=search_query) |
            # OR search in author field (case-insensitive)
            Q(author__icontains=search_query) |
            # OR search in ISBN field (case-insensitive)
            Q(isbn__icontains=search_query)
        )
    
    # Query the database to get all categories
    categories = Category.objects.all()
    # Create a context dictionary to pass data to the template
    context = {
        # Add filtered books to the context
        'books': books,
        # Add categories to the context
        'categories': categories,
        # Add the selected category ID to the context
        'selected_category': category_id,
        # Add the search query to the context
        'search_query': search_query,
    }
    # Render the list.html template with the context data and return the response
    return render(request, 'list.html', context)  


# Define the book_detail view function that takes request and book_id parameters
def book_detail(request, book_id):
    # Docstring describing this view as the book detail page
    """Book detail"""
    # Get the book with the specified ID or return a 404 error if not found
    book = get_object_or_404(Book, id=book_id)
    # Render the detail.html template with the book object and return the response
    return render(request, 'detail.html', {'book': book})  


# Require user to be logged in to access this view
@login_required
# Restrict this view to only accept POST requests
@require_http_methods(["POST"])
# Define the add_to_cart view function that takes request and book_id parameters
def add_to_cart(request, book_id):
    # Docstring describing this view as adding a book to cart
    """Add book to cart"""
    # Start a try block to catch any exceptions
    try:
        # Get the book with the specified ID or return a 404 error if not found
        book = get_object_or_404(Book, id=book_id)
        
        # Check if the book is out of stock
        if book.stock <= 0:
            # Return a JSON response indicating failure with out of stock error
            return JsonResponse({'success': False, 'error': 'Out of Stock'})
        
        # Get the cart from the session, or create an empty dictionary if it doesn't exist
        cart = request.session.get('cart', {})
        
        # Check if the book is already in the cart
        if str(book_id) in cart:
            # Check if adding another would exceed available stock
            if cart[str(book_id)]['quantity'] >= book.stock:
                # Return a JSON response indicating insufficient stock
                return JsonResponse({'success': False, 'error': 'Out of Stock'})
            # Increment the quantity of the existing cart item
            cart[str(book_id)]['quantity'] += 1
        # If book is not in cart yet
        else:
            # Add the book to the cart with initial quantity of 1
            cart[str(book_id)] = {
                # Store the book title
                'title': book.title,
                # Store the book price as a string
                'price': str(book.price),
                # Set initial quantity to 1
                'quantity': 1,
            }
        
        # Update the session cart with the modified cart
        request.session['cart'] = cart
        # Mark the session as modified to ensure it's saved
        request.session.modified = True
        
        # Return a JSON response indicating success with cart count
        return JsonResponse({'success': True, 'cart_count': len(cart)})
    
    # Catch any exceptions that occur
    except Exception as e:
        # Return a JSON response indicating failure with the error message
        return JsonResponse({'success': False, 'error': str(e)})


# Require user to be logged in to access this view
@login_required
# Define the cart view function
def cart(request):
    # Docstring describing this view as the shopping cart
    """Shopping cart"""
    # Get the cart from the session, or create an empty dictionary if it doesn't exist
    cart = request.session.get('cart', {})
    # Initialise an empty list to store cart items with additional data
    cart_items = []
    # Initialise the total amount to zero
    total = Decimal('0.00')
    
    # Iterate through each book ID and item data in the cart
    for book_id, item in cart.items():
        # Start a try block to handle missing books
        try:
            # Get the book object from the database
            book = Book.objects.get(id=book_id)
            # Calculate the subtotal for this cart item
            subtotal = Decimal(item['price']) * item['quantity']
            # Add a dictionary with cart item details to the list
            cart_items.append({
                # Add the book object
                'book': book,
                # Add the quantity
                'quantity': item['quantity'],
                # Add the calculated subtotal
                'subtotal': subtotal,
            })
            # Add the subtotal to the running total
            total += subtotal
        # Catch the exception if the book doesn't exist
        except Book.DoesNotExist:
            # Skip this item and continue to the next
            continue
    
    # Create a context dictionary to pass data to the template
    context = {
        # Add the cart items list to the context
        'cart_items': cart_items,
        # Add the total amount to the context
        'total': total,
    }
    # Render the cart.html template with the context data and return the response
    return render(request, 'cart.html', context)  # Changed!


# Require user to be logged in to access this view
@login_required
# Restrict this view to only accept POST requests
@require_http_methods(["POST"])
# Define the create_order view function
def create_order(request):
    # Docstring describing this view as creating an order
    """Create order"""
    # Get the cart from the session, or create an empty dictionary if it doesn't exist
    cart = request.session.get('cart', {})
    
    # Check if the cart is empty
    if not cart:
        # Return a JSON response indicating failure with empty cart error
        return JsonResponse({'success': False, 'error': 'Empty Cart'})
    
    # Start a try block to catch any exceptions
    try:
        # Get or create a customer object for the current user
        customer, created = Customer.objects.get_or_create(user=request.user)
        # Generate a unique order number using current timestamp
        order_number = f"ORD{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Initialise the total amount to zero
        total = Decimal('0.00')
        # Iterate through each book ID and item data in the cart
        for book_id, item in cart.items():
            # Get the book object from the database
            book = Book.objects.get(id=book_id)
            
            # Check if there's sufficient stock for the requested quantity
            if book.stock < item['quantity']:
                # Return a JSON response indicating insufficient stock for this book
                return JsonResponse({
                    # Set success to False
                    'success': False, 
                    # Include error message with book title
                    'error': f'"{book.title}" is out of stock'
                })
            
            # Add the item's total price to the order total
            total += Decimal(item['price']) * item['quantity']
        
        # Create a new order in the database
        order = Order.objects.create(
            # Set the customer
            customer=customer,
            # Set the order number
            order_number=order_number,
            # Set the total amount
            total_amount=total,
            # Set the shipping address from customer or use default message
            shipping_address=customer.address or "Address need to be confirmed",
        )
        
        # Iterate through each book ID and item data in the cart again
        for book_id, item in cart.items():
            # Get the book object from the database
            book = Book.objects.get(id=book_id)
            # Create an order item for this book
            OrderItem.objects.create(
                # Link to the order
                order=order,
                # Link to the book
                book=book,
                # Set the quantity
                quantity=item['quantity'],
                # Set the price
                price=Decimal(item['price']),
            )
            
            # Decrease the book stock by the ordered quantity
            book.stock -= item['quantity']
            # Save the updated book stock to the database
            book.save()
        
        # Clear the cart by setting it to an empty dictionary
        request.session['cart'] = {}
        # Mark the session as modified to ensure it's saved
        request.session.modified = True
        
        # Return a JSON response indicating success with the order ID
        return JsonResponse({'success': True, 'order_id': order.id})
    
    # Catch any exceptions that occur
    except Exception as e:
        # Return a JSON response indicating failure with the error message
        return JsonResponse({'success': False, 'error': str(e)})

# Require user to be logged in to access this view
@login_required
# Define the order_list view function
def order_list(request):
    # Docstring describing this view as the order list
    """Order list"""
    # Start a try block to handle missing customer
    try:
        # Get the customer object for the current user
        customer = Customer.objects.get(user=request.user)
    # Catch the exception if the customer doesn't exist
    except Customer.DoesNotExist:
        # If customer doesn't exist, create one
        # Create a new customer for the current user
        customer = Customer.objects.create(user=request.user)
    
    # Get orders for this customer
    # Query orders for this customer, ordered by creation date (newest first)
    orders = Order.objects.filter(customer=customer).order_by('-created_at')
    
    # Render the order.html template with the orders data and return the response
    return render(request, 'order.html', {'orders': orders})