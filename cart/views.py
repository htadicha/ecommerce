from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from accounts.models import Account  # If you're using a custom user model

def _get_cart_id(request):
    cart_id = request.session.session_key
    if not cart_id: cart_id = request.session.create()
    return cart_id

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    size = request.POST.get('size')
    quantity = int(request.POST.get('quantity', 1))
    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user, size=size, defaults={'quantity': quantity})
    else:
        cart, _ = Cart.objects.get_or_create(cart_id=_get_cart_id(request))
        cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart, size=size, defaults={'quantity': quantity})
    if not created:
        cart_item.quantity += quantity
    cart_item.save()
    return redirect('cart:cart_detail')

def remove_from_cart(request, cart_item_id):
    # This view is for the '-' button
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_get_cart_id(request))
            cart_item = CartItem.objects.get(id=cart_item_id, cart=cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except ObjectDoesNotExist: pass
    return redirect('cart:cart_detail')

def delete_from_cart(request, cart_item_id):
    # This view is for the 'x' button
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_get_cart_id(request))
            cart_item = CartItem.objects.get(id=cart_item_id, cart=cart)
        cart_item.delete()
    except ObjectDoesNotExist: pass
    return redirect('cart:cart_detail')

def cart_detail(request, total=0, quantity=0, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_get_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for item in cart_items:
            total += (item.product.price * item.quantity)
            quantity += item.quantity
    except ObjectDoesNotExist: pass
    context = {'cart_items': cart_items, 'total': total, 'quantity': quantity}
    return render(request, 'cart/shopping_cart.html', context)

def update_cart(request):
    """
    Handles updating quantities of all items in the cart at once.
    """
    if request.method == 'POST':
        for key, value in request.POST.items():
            # Check for keys that start with 'quantity_' to identify cart items
            if key.startswith('quantity_'):
                try:
                    # Extract the cart_item_id from the key (e.g., 'quantity_12' -> 12)
                    cart_item_id = int(key.split('_')[1])
                    quantity = int(value)
                    
                    # Security check: ensure the cart item belongs to the current user
                    if request.user.is_authenticated:
                        cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)
                    else:
                        cart = Cart.objects.get(cart_id=_get_cart_id(request))
                        cart_item = CartItem.objects.get(id=cart_item_id, cart=cart)

                    if quantity > 0:
                        # Update the quantity and save
                        cart_item.quantity = quantity
                        cart_item.save()
                    else:
                        # If quantity is 0 or less, remove the item from the cart
                        cart_item.delete()
                except (CartItem.DoesNotExist, ValueError):
                    # Handle cases where the item doesn't exist or value is not a valid number
                    pass
        messages.success(request, 'Your cart has been updated.')
    return redirect('cart:cart_detail')
