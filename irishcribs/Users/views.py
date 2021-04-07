from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})


def login(request):
	return render(request, 'registration/login.html')

def accountPage(request):
	user = request.user

	return render(request, 'profile.html', {'user': user})
