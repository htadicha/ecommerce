from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'required': 'required',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'required': 'required',
    }))

    def clean(self):
        # Add custom validation if needed (e.g., check if user exists)
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        # You can validate credentials here.
        return cleaned_data


class SignupForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
        'required': 'required',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Create password',
        'required': 'required',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        'required': 'required',
    }))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Passwords do not match.")
        
        # Add more validation like password strength if needed
        return cleaned_data

