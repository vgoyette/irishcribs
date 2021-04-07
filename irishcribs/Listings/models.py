#!/usr/bin/python3
from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.

class Listing(models.Model):
	address = models.CharField(max_length=100, default='1 Compton Family Ice Arena, Notre Dame, IN 46556')
	#lister = models.ForeignKey(User, on_delete=models.CASCADE)
	lister = models.CharField(max_length=40, default="admin")
	startDate = models.CharField(max_length=40, default='December 31st, 2021')
	endDate = models.CharField(max_length=40, default='January 1st, 2022')
	rent = models.FloatField(default=0)
	bedrooms = models.FloatField(default=0)
	bathrooms = models.FloatField(default=0)
	sqft = models.FloatField(default=0)
	isApartment = models.IntegerField(default=0)
	website = models.CharField(max_length=50, default="http://www.nd.edu")
	comments = models.CharField(max_length=100, default="")
	
	def __str__(self):
		return str(self.address)


class listing_library():
	
	def edit_listing(listing=None, address="", startDate="", endDate="", rent=-1, bedrooms=-1, bathrooms=-1, sqft=-1, isApartment=-1, website="", comments=""):
		# 0 is house, 1 is apartment
		rAddr = None

		# Build query for an update
		query = "UPDATE Listings SET "


		# This way of building the query is pretty gross, but it allows us to control for if only a few attributes are changing and not all of them.
		# It's ugly, but it works
		if listing is not None:

			if address == "":
				query = query + "Address='" + str(listing.address) + "', "
				rAddr = str(listing.address)
			else:
				query = query + "address='" + str(address) + "', "
				rAddr = str(address)


			if startDate == "":
				query = query + "StartDate='" + str(listing.startDate) + "', "
			else:
				query = query + "StartDate='" + str(startDate) + "', "
			

			if endDate == "":
				query = query + "EndDate='" + str(listing.endDate) + "', "
			else:
				query = query + "EndDate='" + str(endDate) + "', "


			if rent == -1:
				query = query + "ListingPrice=" + str(listing.rent) + ", "
			else:
				query = query + "ListingPrice=" + str(rent) + ", "


			if bedrooms == -1:
				query = query + "Bedrooms=" + str(listing.bedrooms) + ", "
			else:
				query = query + "Bedrooms=" + str(bedrooms) + ", "


			if bathrooms == -1:
				query = query + "Bathrooms=" + str(listing.bathrooms) + ", "
			else:
				query = query + "Bathrooms=" + str(bathrooms) + ", "


			if sqft == -1:
				query = query + "SqFt=" + str(listing.sqft) + ", "
			else:
				query = query + "SqFt=" + str(sqft) + ", "


			if isApartment == -1:
				query = query + "ApartmentBool=" + str(listing.isApartment) + ", "
			else:
				query = query + "ApartmentBool=" + str(isApartment) + ", "


			if website == "":
				query = query + "Website='" + str(listing.website) + "', "
			else:
				query = query + "Website='" + str(website) + "', "


			if comments == "":
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



temp_l = Listing(address="4000 Braemore Ave, Roseland, IN 46556",
				 lister="vgoyette",
				 startDate="June 1st, 2021",
				 endDate="May 30th, 2022",
				 rent=1400,
			     bedrooms=4,
				 bathrooms=3,  
				 sqft=1000,
				 isApartment=1,
				 website="www.universityedgend.com",
				 comments="This place is literally destroyed"
				)

print(listing_library.add_listing("4000 Braemore Ave, Roseland, IN 46556",
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
))

print(listing_library.delete_listing(temp_l))
