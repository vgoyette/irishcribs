from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse
from .models import Listing, listing_library#, EditForm, AddForm, FilterForm, listing_library
from .forms import AddForm, EditForm, FilterForm
import json
import logging
import pdb
import datetime

from django.contrib.auth.decorators import login_required

logger=logging.getLogger(__name__)
lib = listing_library()

def convert(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

# Create your views here.

def view_listings(request):
    # The "get_all_listings" function from our custom library executes a SQL statement to retrieve all listings
    listings = lib.get_all_listings()
    return render(request, 'show_listing.html', {'listings': listings})

@login_required
def add_listings(request):
    form = None
    if request.method == 'POST':
        user = request.user
        form = AddForm(request.POST)
        if form.is_valid():
			# This looks gross, but it's just to make the "add_listing" function call a bit prettier
            address     = form.cleaned_data['address']
            lister      = user
            startDate   = form.cleaned_data['startDate']
            endDate     = form.cleaned_data['endDate']
            rent        = form.cleaned_data['rent']
            bedrooms    = form.cleaned_data['bedrooms']
            bathrooms   = form.cleaned_data['bathrooms']
            sqft        = form.cleaned_data['sqft']
            isApartment = form.cleaned_data['isApartment']
            website     = form.cleaned_data['website']
            comments    = form.cleaned_data['comments']
            lib.add_listing(address, lister, startDate, endDate, rent, bedrooms, bathrooms, sqft, isApartment, website, comments)
            return redirect('home')
    else:
        form = AddForm()
    
    return render(request, 'add_listing.html', {'form': form})


class EditListingView(UpdateView):
    model = Listing
    fields = ['address',
              'startDate',
			  'rent',
              'endDate',
              'bedrooms', 
              'bathrooms', 
              'sqft',
              'isApartment',
              'website', 
              'comments']

    
    template_name = 'listing_update_form.html'
    
    def get_success_url(self):
        return reverse('home')


class DeleteListingView(DeleteView):
    model = Listing

    template_name = 'listing_confirm_delete.html'

    def get_success_url(self):
        return reverse('home')

'''@login_required
def edit_listing(request, address):
    user = request.user

    userListings = list(Listing.objects.filter(lister=user))
    
    if user.is_authenticated:
        if request.method == 'POST':
            form = EditForm(request.POST)
            if form.is_valid():
                #listing_library.edit_listing(listing=None, address=None, startDate=None, endDate=None, rent=None, bedrooms=None, bathrooms=None, sqft=None, isApartment=None, website=None, comments=None)
                form.save()
                return HttpResponseRedirect('editthanks')
        else:
            form = EditForm()
    
    return render(request, 'edit_listing.html', {'form': form})'''

def filter_listing_form(request):
    minBeds  = 0
    minBaths = 0
    maxRent  = 5000
    minSqft  = 0
    apt      = -1
    listings = None

    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['bedrooms']:
                minBeds = form.cleaned_data['bedrooms']
            if form.cleaned_data['bathrooms']:
                minBaths = form.cleaned_data['bathrooms']
            if form.cleaned_data['rent']:
                maxRent = form.cleaned_data['rent']
            if form.cleaned_data['sqft']:
                minSqft = form.cleaned_data['sqft']
            if form.cleaned_data['isApartment']:
                apt = form.cleaned_data['isApartment']

            listings = lib.filter_listings(minBeds, minBaths, maxRent, minSqft, apt)

            filtered_listings = []
            for listing in listings:
                d = {}
                d['address'] = listing[0]
                #d['startDate'] = listing[1].strftime("%m/%d/%y")
                #pdb.set_trace()
                #d['endDate'] = listing[2].strftime("%m/%d/%y")
                d['rent'] = listing[3]
                d['bedrooms'] = listing[4]
                d['bathrooms'] = listing[5]
                d['sqft'] = listing[6]
                d['apt'] = listing[7]
                d['website'] = listing[8]
                d['comments'] = listing[9]
                filtered_listings.append(d)
            
            

            request.session['filtered_listings'] = filtered_listings
            return redirect('filtered_listings')
    else:
        form = FilterForm()

    return render(request, 'filter_listing_form.html', {'form': form})    


# This is the function to actually display the filtered listings to the user
def filtered_listings(request):
    listings = request.session['filtered_listings']

    return render(request, 'filter_listing.html', {'listings' : listings})
         
