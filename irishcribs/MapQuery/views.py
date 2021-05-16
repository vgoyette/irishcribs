from django.shortcuts import render, redirect
from django.http import HttpResponse
from Listings.models import Listing, listing_library
import googlemaps
import json
import datetime

gmaps = googlemaps.Client('AIzaSyBVYADTq8rJ8_7sl4QrOOB0Se_mnOCHDxg')
lib = listing_library()

# This is the function to actually display the filtered listings to the user
def map_query(request):

	#if request.is_ajax():
	listings = lib.get_all_listings()

	area_listings = []

	if request.is_ajax():
		n_bound = float(request.POST.get('north', 0))
		e_bound = float(request.POST.get('east', 0))
		s_bound = float(request.POST.get('south', 0))
		w_bound = float(request.POST.get('west', 0))

		for listing in listings:
			results = gmaps.geocode(listing.address)
			lat = results[0]['geometry']['location']['lat']
			lng = results[0]['geometry']['location']['lng']

			if lat <= n_bound and lat >= s_bound and lng <= e_bound and lng >= w_bound:
				d = {}
				d['address']     = listing.address
				d['lister']      = listing.lister_id
				d['startDate']   = listing.startDate.strftime("%m/%d/%y")
				d['endDate']     = listing.endDate.strftime("%m/%d/%y")
				d['rent']        = listing.rent
				d['bedrooms']    = listing.bedrooms
				d['bathrooms']   = listing.bathrooms
				d['sqft']        = listing.sqft
				d['isApartment'] = listing.isApartment
				d['website']     = listing.website
				d['comments']    = listing.comments
				d['lat'] = lat
				d['lng'] = lng
				area_listings.append(d)

		return HttpResponse(json.dumps(area_listings), content_type='application/json')


	return render(request, 'map_query.html')

def area_listing(request):
	return render(request, 'area_listing.html')
