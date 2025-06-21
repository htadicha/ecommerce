from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator

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
		# Use Django's send_mail function for git_hub vistors to my site
		try:
			send_mail(
				f"Contact Form: {subject}", # Email subject
				full_message, # Email body
				'noreply@domain.com', # From email (can be a generic no-reply address)
				['mail_admin_email@example.com'], # To email (REPLACE with your actual email)
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
    # This query now filters for products that are new, on deal, OR on clearance.
    # It also ensures they are available and orders them by newest first.
    products = Product.objects.filter(
        Q(is_new=True) | Q(is_on_deal=True) | Q(is_clearance=True),
        is_available=True
    ).order_by('-id')

    context = {'products': products}
    return render(request, 'store/index.html', context)

# In store/views.py, make sure to import Paginator
from django.core.paginator import Paginator

def product_list(request):
    # Get all products initially
    products_list = Product.objects.filter(is_available=True).order_by('name')

    # Search functionality
    query = request.GET.get('q')
    if query:
        products_list = products_list.filter(Q(name__icontains=query) | Q(main_description__icontains=query))

    # Sorting functionality
    sort_by = request.GET.get('sort')
    if sort_by == 'price':
        products_list = products_list.order_by('price')
    elif sort_by == 'ratings':
        products_list = products_list.order_by('-ratings')
    elif sort_by == 'name':
        products_list = products_list.order_by('name')
        
    product_count = products_list.count()

    # --- Pagination Logic ---
    paginator = Paginator(products_list, 12)  # Show 10 products per page.
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    # --- End of Pagination Logic ---

    context = {
        'products': products, # This now sends the paginated page object
        'product_count': product_count,
        'query': query,
        'sort_by': sort_by, # Pass sort_by to preserve it in pagination links
    }
    return render(request, 'store/categories.html', context)

def product_detail(request, category_id, product_id):
	product = get_object_or_404(Product, category__id=category_id, id=product_id)
	return render(request, 'store/product-page.html', {'product': product})