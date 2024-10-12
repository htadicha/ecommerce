from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from .forms import LoginForm, SignupForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from .models import Customer 

def store(request):
    query = request.GET.get('q')  # Get the search query from the URL
    if query:
        # Filter products based on the query
        products = Product.objects.filter(name__icontains=query)
    else:
        # If no query is provided, show all products
        products = Product.objects.all()
    
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    # Pass the filtered or all products to the template, along with the query
    context = {'products': products, 'cartItems': cartItems, 'query': query}
    return render(request, 'store/store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.filter(id=productId).first()  # Use .first() to prevent NoneType errors

	if product:  # Only proceed if product exists
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

		if action == 'add':
			orderItem.quantity = (orderItem.quantity + 1)
		elif action == 'remove':
			orderItem.quantity = (orderItem.quantity - 1)

		orderItem.save()

		if orderItem.quantity <= 0:
			orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)



# Create your views here.

User = get_user_model()

def login_view(request):
    # Ensure form is initialized outside the POST check to handle GET requests
    form = LoginForm(request.POST or None)  # If it's a GET request, create an empty form
    
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('store')  # Redirect to the store after successful login
            else:
                form.add_error(None, "Invalid login credentials")  # Show error on invalid credentials
    # Render the login form even on GET or invalid POST
    return render(request, 'store/login.html', {'form': form})

def signup_view(request):
    form = SignupForm(request.POST or None)  # Create an empty form on GET

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            # Create the user using the email as the username
            user = User.objects.create_user(username=email, email=email, password=password)
            
            # Automatically create a Customer associated with this User
            Customer.objects.create(user=user, name=user.username, email=user.email)
            
            # Log in the user after signup
            login(request, user)
            return redirect('store')  # Redirect to the store after successful signup
    
    # Render the signup form even on GET or invalid POST
    return render(request, 'store/sign_up.html', {'form': form})

def logout_view(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to login page after logout

def home_view(request):
    return render(request, 'store.html')  # Render the home view
