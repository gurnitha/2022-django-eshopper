# users/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.forms import AuthenticationForm

# Locals
from users.models import UserCreateForm

# Create your views here.

def signup(request):

	if request.method == 'POST':
		form = UserCreateForm(request.POST)

		if form.is_valid():
			new_user = form.save()
			new_user = authenticate(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password1'],
			)
			dj_login(request,new_user)
			return redirect('index')
	else:
		form = UserCreateForm()

	context = {
		'form':form
	}
	
	return render(request, 'registration/signup.html', context)


# def login(request):

# 	# if request.method == 'GET':
# 	# 	return render(request, 'users/registration/login.html', {'form':AuthenticationForm})

# 	# else:
# 	# 	user = authenticate(request,
# 	# 			username=request.POST['username'],
# 	# 			password=request.POST['password'])

# 	# 	if user is None:
# 	# 		return render(request,'users/registration/login.html', {'form': AuthenticationForm(), 'error': 'username and password do not match'})
	
# 	# 	else:
# 	# 		dj_login(request,user)
# 	# 		return redirect('index')


def logout(request):
	dj_logout(request)
	return redirect('index')