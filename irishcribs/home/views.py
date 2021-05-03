from django.shortcuts import render
from Listings.models import Listing

def home(request):
	listings = Listing.objects.all()
	return render(request, 'show_listing.html', {'listings' : listings})
