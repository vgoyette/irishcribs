from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.db import connection
import mysql.connector
from Listings.models import Listing

# Create your views here.

cnx = mysql.connector.connect(user='djangouser', password='pw', database='Listings')
cursor = cnx.cursor()

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
	id = user.id

	query = "SELECT * FROM Listings_listing, auth_user WHERE Listings_listing.lister_id=auth_user.id AND Listings_listing.lister_id=%s"
	listings = Listing.objects.raw(query, [id])
	username = None
	for listing in listings:
		username = listing.username
		break


	return render(request, 'profile.html', {'user': user, 'listings': listings, 'username' : username})
