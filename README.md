Online Bookstore

A full-featured online bookstore built with Django that allows users to browse books, manage shopping carts, and place orders.

Features

- User Authentication: Secure login and logout functionality
- Book Browsing: View and search through available books
- Category Filtering: Filter books by categories
- Shopping Cart: Add books to cart and manage quantities
- Order Management: Place orders and view order history
- Admin Panel: Manage books, categories, and orders through Django admin
- Responsive Design: Clean UI with Poppins font and gradient styling

Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- Database: SQLite (default Django database)
- Styling: Custom css

Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

Installation

1. Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd bookstore
   ```

2. Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies**
   ```bash
   pip install django
   ```

5. Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser (admin account)
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set username, email, and password.

7. Run the development server
   ```bash
   python manage.py runserver
   ```

8. Access the application
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

Database Models

Book
- Title
- Author
- Category (Foreign Key)
- Price
- Description
- Cover image

Category
- Name
- Description

Cart
- User (Foreign Key)
- Book (Foreign Key)
- Quantity

Order
- User (Foreign Key)
- Order date
- Total amount
- Status (Pending, Confirmed, Shipped, Delivered)

Features in Detail

For Customers
1. Browse Books**: View all available books on the homepage
2. Search: Search for books by title or author
3. Filter: Filter books by category
4. Add to Cart: Click "Add to Cart" to add books
5. Manage Cart: View and update cart items
6. Place Orders: Checkout and place orders
7. Order History: View past orders and their status

For Admins
1. Book Management: Add, edit, and delete books
2. Category Management: Create and manage book categories
3. Order Management: View and update order statuses
4. User Management: Manage user accounts

User Roles

- Guest Users: Can browse books but cannot add to cart or place orders
- Registered Users: Can browse, add to cart, and place orders
- Admin Users: Full access to Django admin panel

Usage

Adding Books (Admin)
1. Login to admin panel at `/admin/`
2. Navigate to "Books"
3. Click "Add Book"
4. Fill in book details and save

Shopping (User)
1. Register or login to your account
2. Browse books or use search/filter
3. Click "Add to Cart" on desired books
4. Go to Cart to review items
5. Proceed to checkout and place order
6. View order status in "My Orders"