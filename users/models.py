# users/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
from django import forms
from django.forms import ValidationError

# Create your models here.

class UserCreateForm(UserCreationForm):
	email = forms.EmailField(
		required=True, label='email',
		error_messages={'exists': 'This email already exists'})

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(UserCreateForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user 

	def clean_email(self):
		if User.objects.filter(email=self.cleaned_data['email']).exists():
			raise form.ValidationError(self.fields['email'].error_messages['exists'])
		return self.cleaned_data['email']