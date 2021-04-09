#!/usr/bin/python3
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


import uuid

# Create your models here.

class Listing(models.Model):
	address = models.CharField(max_length=100, primary_key=True)
	lister = models.ForeignKey(User, on_delete=models.CASCADE)
	startDate = models.DateField(blank=True, null=True)
	endDate = models.DateField(blank=True, null=True)
	rent = models.FloatField(blank=True, null=True)
	bedrooms = models.FloatField(blank=True, null=True)
	bathrooms = models.FloatField(blank=True, null=True)
	sqft = models.FloatField(blank=True, null=True)
	isApartment = models.IntegerField(blank=True, null=True)
	website = models.CharField(max_length=50, blank=True, null=True)
	comments = models.CharField(max_length=100, blank=True, null=True)
	
	def __str__(self):
		return str(self.address)


	
#class EditForm(ModelForm):
#    class Meta:
#        model = Listing
#        exclude = ['lister']

#class AddForm(ModelForm):
#    class Meta:
#        model = Listing
#        exclude = ['lister']

#class FilterForm(ModelForm):#
#	class Meta:
#		model = Listing
#		fields = ['bedrooms',
#				  'bathrooms',
#				  'rent',
#				  'sqft',
#				  'isApartment']



class listing_library():
	
	def edit_listing(listing=None, address=None, startDate=None, endDate=None, rent=None, bedrooms=None, bathrooms=None, sqft=None, isApartment=None, website=None, comments=None):
		# 0 is house, 1 is apartment
		rAddr = None

		# Build query for an update
		query = "UPDATE Listings SET "


		# This way of building the query is pretty gross, but it allows us to control for if only a few attributes are changing and not all of them.
		# It's ugly, but it works
		if listing is not None:

			if address == None:
				query = query + "Address='" + str(listing.address) + "', "
				rAddr = str(listing.address)
			else:
				query = query + "address='" + str(address) + "', "
				rAddr = str(address)


			if startDate == None:
				query = query + "StartDate='" + str(listing.startDate) + "', "
			else:
				query = query + "StartDate='" + str(startDate) + "', "
			

			if endDate == None:
				query = query + "EndDate='" + str(listing.endDate) + "', "
			else:
				query = query + "EndDate='" + str(endDate) + "', "


			if rent == None:
				query = query + "ListingPrice=" + str(listing.rent) + ", "
			else:
				query = query + "ListingPrice=" + str(rent) + ", "


			if bedrooms == None:
				query = query + "Bedrooms=" + str(listing.bedrooms) + ", "
			else:
				query = query + "Bedrooms=" + str(bedrooms) + ", "


			if bathrooms == None:
				query = query + "Bathrooms=" + str(listing.bathrooms) + ", "
			else:
				query = query + "Bathrooms=" + str(bathrooms) + ", "


			if sqft == None:
				query = query + "SqFt=" + str(listing.sqft) + ", "
			else:
				query = query + "SqFt=" + str(sqft) + ", "


			if isApartment == None:
				query = query + "ApartmentBool=" + str(listing.isApartment) + ", "
			else:
				query = query + "ApartmentBool=" + str(isApartment) + ", "


			if website == None:
				query = query + "Website='" + str(listing.website) + "', "
			else:
				query = query + "Website='" + str(website) + "', "


			if comments == None:
				query = query + "Comments='" + str(listing.comments) + "', "
			else:
				query = query + "Comments='" + str(comments) + "', "

			# Add a where clause to make sure the correct address is updated			
			query = query + " WHERE address='" + rAddr + "';"
			return query

	def add_listing(address, lister, start, end, rent, bedrooms, bathrooms, sqft, isApartment, website, comments):
		l = Listing(address=address, 
					lister=lister,
					startDate=start,
					endDate=end,
					rent=rent,
					bedrooms=bedrooms,
					bathrooms=bathrooms,
					sqft=sqft,
					isApartment=isApartment,
					website=website,
					comments=comments)
		
		query = f"""INSERT INTO Listings (Address, Lister, StartDate, EndDate, ListingPrice, Bedrooms, Bathrooms, SqFt, ApartmentBool, Website, Comments) VALUES 
('{l.address}', '{l.lister}', '{l.startDate}', '{l.endDate}', {l.rent}, {l.bedrooms}, {l.bathrooms}, {l.sqft}, {l.isApartment}, '{l.website}', '{l.comments}'); """
		return query

	def delete_listing(listing):
		addr = listing.address

		query = f"""DELETE FROM Listings WHERE Address='{addr}'"""

		return query

	
	def filter_listings(minBedrooms=0, minBathrooms=0, maxRent=5000, minSqft=0, isApartment=-1):
		beds = minBedrooms
		baths = minBathrooms
		rent = maxRent
		sqft = minSqft
		apt = isApartment


		# If the user specifies the type of listing (i.e. apartment or house), only those types of listings are searched for
		if isApartment == -1:
			query = f"""SELECT * FROM Listings WHERE Bedrooms>={beds} AND Bathrooms>={baths} AND ListingPrice<={rent} AND SqFt>={sqft};"""
		# If the user doesn't specify, then all listings meeting the other params are returned
		else:
			query = f"""SELECT * FROM Listings WHERE Bedrooms>={beds} AND Bathrooms>={baths} AND ListingPrice<={rent} AND SqFt>={sqft} AND ApartmentBool={apt};"""


		return query


	def get_all_listings():
		query = f"""SELECT Address, StartDate, EndDate, ListingPrice, Bedrooms, Bathrooms, SqFt, ApartmentBool, Website, Comments FROM Listings"""

		return query

'''print(listing_library.add_listing("4000 Braemore Ave, Roseland, IN 46556",
				 "vgoyette",
				 "June 1st, 2021",
				 "May 30th, 2022",
				 1400,
			     4,
				 3,  
				 1000,
				 1,
				 "www.universityedgend.com",
				 "This place is literally destroyed"
))'''