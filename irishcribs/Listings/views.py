from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse
from .models import Listing#, EditForm, AddForm, FilterForm, listing_library
from .forms import AddForm, EditForm, FilterForm
import json
import logging
import pdb
import datetime

from django.contrib.auth.decorators import login_required

logger=logging.getLogger(__name__)

def convert(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

# Create your views here.

def view_listings(request):
    listings = Listing.objects.all()

    return render(request, 'show_listing.html', {'listings': listings})

@login_required
def add_listings(request):
    form = None
    if request.method == 'POST':
        user = request.user
        form = AddForm(request.POST)
        if form.is_valid():
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
            #listing = form.save(commit=False)         # REMOVE LATER WHEN DATABASE IS SET UP
            #listing.lister = request.user
            #listing.save()
            #listing_library.add_listing(address, lister, startDate, endDate, rent, bedrooms, bathrooms, sqft, isApartment, website, comments)
            l = Listing(address=address, lister=lister, startDate=startDate, endDate=endDate, rent=rent, bedrooms=bedrooms, bathrooms=bathrooms, sqft=sqft, isApartment=isApartment, website=website, comments=comments)
            l.save()
            return redirect('home')
    else:
        form = AddForm()
    
    return render(request, 'add_listing.html', {'form': form})


class EditListingView(UpdateView):
    model = Listing
    fields = ['address',
              'startDate',
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
    apt      = 1
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

            listings = Listing.objects.filter(bedrooms__gte=minBeds,
                                              bathrooms__gte=minBaths,
                                              rent__lte=maxRent,
                                              sqft__gte=minSqft,
                                              isApartment=apt,
                                            )
            
            filtered_listings = []
            for l in listings:
                d = {}
                d['address'] = l.address
                d['startDate'] = l.startDate.strftime("%m/%d/%y")
                #pdb.set_trace()
                d['endDate'] = l.endDate.strftime("%m/%d/%y")
                d['bedrooms'] = l.bedrooms
                d['bathrooms'] = l.bathrooms
                d['rent'] = l.rent
                d['sqft'] = l.sqft
                d['apt'] = l.isApartment
                d['website'] = l.website
                d['comments'] = l.comments
                filtered_listings.append(d)
            
            

            request.session['filtered_listings'] = filtered_listings
            #filtered_list = listing_library.filter_listings(minBedrooms=minBeds, minBathrooms=minBaths, maxRent=maxRent, minSqft=minSqft, isApartment=apt)
            return redirect('filtered_listings')
    else:
        form = FilterForm()

    return render(request, 'filter_listing_form.html', {'form': form})    


def filtered_listings(request):
    listings = request.session['filtered_listings']

    

    return render(request, 'filter_listing.html', {'listings' : listings})
         