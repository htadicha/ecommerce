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
	
	"""
Render the store view with product filtering.

- Retrieves search query from the URL and filters products based on it.
- If no query is provided, displays all products.
- Includes cart data in the context for rendering.
- Returns the store template with the filtered products and cart information.
"""

	query = request.GET.get('q') 
	if query:
		
		products = Product.objects.filter(name__icontains=query)
	else:
		
		products = Product.objects.all()
	
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	
	context = {'products': products, 'cartItems': cartItems, 'query': query}
	return render(request, 'store/store.html', context)


def cart(request):
	"""
Render the cart and checkout views.

- cart: Retrieves cart data and renders the cart template with items, order, and item count.
- checkout: Retrieves cart data and renders the checkout template with items, order, and item count.
"""

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
	
	
	"""
Update item quantity in the user's order.

- Parses request data for product ID and action (add/remove).
- Retrieves the customer and product, updates the order and order item.
- Adjusts quantity or deletes the item if quantity is zero.
- Returns a JSON response confirming the update.
"""

	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.filter(id=productId).first()  

	if product: 
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
	
	"""
Process orders and handle payment.

- Retrieves or creates an order for authenticated users or processes guest orders.
- Verifies and completes the order if the total matches.
- Saves the order and creates a shipping address if needed.
- Returns a JSON response confirming payment submission.
"""
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





User = get_user_model()


"""
Handle user login and signup.

Functions:
- login_view: Renders the login form, authenticates the user on POST, and logs them in if credentials are valid. Redirects to the store on success or displays an error on failure.
- signup_view: Renders the signup form, creates a new user and customer, and logs the user in after successful signup.
"""

def login_view(request):
	
	form = LoginForm(request.POST or None)  
	
	if request.method == 'POST':
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=email, password=password)
			if user is not None:
				login(request, user)
				return redirect('store')  
			else:
				form.add_error(None, "Invalid login credentials")  
	return render(request, 'store/login.html', {'form': form})

def signup_view(request):
	
	"""
Handle user signup, logout, and home page rendering.

Functions:
- signup_view: Renders the signup form, processes the signup request, creates a new user and customer, and logs the user in.
- logout_view: Logs the user out and redirects to the login page.
- home_view: Renders the homepage.
"""
	form = SignupForm(request.POST or None)  

	if request.method == 'POST':
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			
			user = User.objects.create_user(username=email, email=email, password=password)
			
			
			Customer.objects.create(user=user, name=user.username, email=user.email)
			
		
			login(request, user)
			return redirect('store')  
	
	
	return render(request, 'store/sign_up.html', {'form': form})

def logout_view(request):
	logout(request)  
	return redirect('login')  

def home_view(request):
	return render(request, 'store.html')  
