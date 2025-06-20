from django.shortcuts import render, redirect
from cart.models import CartItem
from .forms import OrderForm
from .models import Order, OrderProduct
import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items: return redirect('store:product_list')
    total = sum(item.sub_total() for item in cart_items)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.order_total = total
            order.ip = request.META.get('REMOTE_ADDR')
            order.save()
            # Generate order number
            order.order_number = f"{datetime.date.today().strftime('%Y%m%d')}{order.id}"
            order.save()
            # Move cart items to OrderProduct
            for item in cart_items:
                OrderProduct.objects.create(order=order, user=request.user, product=item.product, quantity=item.quantity, product_price=item.product.price, ordered=True)
            cart_items.delete()
            # Send email
            mail_subject = 'Thank you for your order!'
            message = render_to_string('orders/order_received_email.html', {'user': request.user, 'order': order})
            send_email = EmailMessage(mail_subject, message, to=[request.user.email])
            send_email.send()
            return render(request, 'orders/order_confirmation.html', {'order': order})
    return render(request, 'orders/check-out.html', {'cart_items': cart_items, 'total': total})
