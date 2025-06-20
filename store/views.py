from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib import messages

# Add this new view function to the end of store/views.py
def contact(request):
	if request.method == 'POST':
		# Get the form data from the request
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		from_email = request.POST.get('email')
		subject = request.POST.get('subject')
		message_body = request.POST.get('message')

		# Construct the full message to be sent
		full_message = f"""
		New contact message from: {first_name} {last_name}
		Reply-to Email: {from_email}
		------------------------------------------
		Message:
		{message_body}
		"""
		# Use Django's send_mail function
		try:
			send_mail(
				f"Contact Form: {subject}", # Email subject
				full_message, # Email body
				'noreply@yourdomain.com', # From email (can be a generic no-reply address)
				['your_admin_email@example.com'], # To email (REPLACE with your actual email)
				fail_silently=False,
			)
			messages.success(request, 'Thank you for your message! We will get back to you shortly.')
		except Exception as e:
			messages.error(request, 'There was an error sending your message. Please try again later.')
			# For debugging, it's helpful to see the error in the console
			print(e) 

		return redirect('store:contact')

	return render(request, 'store/contact.html')

def home(request):
	products = Product.objects.filter(is_available=True).order_by('-ratings')[:8]
	context = {'products': products}
	return render(request, 'store/index.html', context)

def product_list(request):
	products = Product.objects.filter(is_available=True).order_by('name')
	product_count = products.count()
	query = request.GET.get('q')
	if query:
		products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
		product_count = products.count()
	sort_by = request.GET.get('sort')
	if sort_by == 'price': products = products.order_by('price')
	elif sort_by == 'ratings': products = products.order_by('-ratings')
	context = {'products': products, 'product_count': product_count, 'query': query}
	return render(request, 'store/categories.html', context)

def product_detail(request, category_id, product_id):
	product = get_object_or_404(Product, category__id=category_id, id=product_id)
	return render(request, 'store/product-page.html', {'product': product})