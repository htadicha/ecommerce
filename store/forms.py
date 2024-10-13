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
		cleaned_data = super().clean()
		email = cleaned_data.get('email')
		password = cleaned_data.get('password')
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
		
		"""
Validate form data after field-level validation.

Compares the provided password and confirm_password fields to ensure they match. 
Raises a ValidationError if they do not match. Additional validation can be added, 
such as checking password strength.

Returns:
	dict: A dictionary containing the cleaned data.

Raises:
	ValidationError: If the passwords do not match.
"""
		cleaned_data = super().clean()
		password = cleaned_data.get('password')
		confirm_password = cleaned_data.get('confirm_password')

		if password != confirm_password:
			raise ValidationError("Passwords do not match.")
		
		# Add more validation like password strength if needed
		return cleaned_data

