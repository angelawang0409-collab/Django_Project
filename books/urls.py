# Import path for URL routing and views from current app
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# Define app namespace for URL reversing
app_name = 'Django_bookstore'

# URL patterns mapping URLs to view functions
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Homepage
    path('books/', views.book_list, name='book_list'),  # All books
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),  # Single book detail
    path('cart/', views.cart, name='cart'),  # Shopping cart
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),  # Add to cart
    path('create-order/', views.create_order, name='create_order'),  # Checkout/create order
    path('orders/', views.order_list, name='order_list'),  # Order history
]

# Serve media files (e.g. uploaded book cover images) during development only.
# When DEBUG is True, Django uses this to map MEDIA_URL to MEDIA_ROOT.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


