from .models import Cart, CartItem
from .views import _get_cart_id
from django.core.exceptions import ObjectDoesNotExist

def cart_counter(request):
    """
    A context processor to make the cart item count available on all pages.
    """
    cart_count = 0
    if 'admin' in request.path:
        return {} # Exit early for admin pages to avoid unnecessary queries

    try:
        # Check for authenticated users first
        if request.user.is_authenticated:
            # THE FIX: Instead of passing the whole request.user object,
            # we explicitly use the user's ID for the database query.
            # This is more robust and avoids potential proxy object issues.
            cart_items = CartItem.objects.filter(user_id=request.user.id, is_active=True)
        # Handle anonymous users
        else:
            # Get the cart based on the session ID
            cart = Cart.objects.get(cart_id=_get_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        
        # Sum the quantity of all items found
        cart_count = sum(item.quantity for item in cart_items)
    except (Cart.DoesNotExist, AttributeError):
        # If the cart does not exist for an anonymous user, or if request.user
        # has an issue (like no 'id'), the count is 0.
        cart_count = 0
    
    return dict(cart_count=cart_count)