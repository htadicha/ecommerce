from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

def register(request):
    """
    Handles new user registration.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Create the username from the email address
            username = email.split('@')[0]

            # --- THIS IS THE DEFINITIVE FIX ---
            # We must explicitly call our custom 'create_user' method from the model manager.
            # This ensures all the logic inside MyAccountManager (like setting is_active=True) is executed.
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            
            # Now, save the additional field
            user.phone_number = phone_number
            user.save()
            
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('accounts:login')
    else:
        form = RegistrationForm()
        
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def login_view(request):
    """
    Handles the user login process.
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('store:product_list')
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('accounts:login')
    return render(request, 'accounts/login.html')


@login_required(login_url='accounts:login')
def logout_view(request):
    """
    Handles user logout.
    """
    auth.logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('accounts:login')
