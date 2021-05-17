#!/usr/bin/python3
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import connection
import mysql.connector
import uuid

# Create your models here.

cnx = mysql.connector.connect(user='vgoyette', password='vgoyette', database='vgoyette')
cursor = cnx.cursor()

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
	website = models.CharField(max_length=200, blank=True, null=True)
	comments = models.CharField(max_length=100, blank=True, null=True)
	
	def __str__(self):
		return str(self.address)

class listing_library():
	
	def edit_listing(self, listing=None, address=None, startDate=None, endDate=None, rent=None, bedrooms=None, bathrooms=None, sqft=None, isApartment=None, website=None, comments=None):
		# 0 is house, 1 is apartment
		rAddr = None

		# Build query for an update
		query = "UPDATE Listings_listing SET "


		# This way of building the query is pretty gross, but it allows us to control for if only a few attributes are changing and not all of them.
		# It's ugly, but it works
		if listing is not None:

			if address == None:
				query = query + "address='" + str(listing.address) + "', "
				rAddr = str(listing.address)
			else:
				query = query + "address='" + str(address) + "', "
				rAddr = str(address)


			if startDate == None:
				query = query + "startDate='" + str(listing.startDate) + "', "
			else:
				query = query + "startDate='" + str(startDate) + "', "
			

			if endDate == None:
				query = query + "endDate='" + str(listing.endDate) + "', "
			else:
				query = query + "endDate='" + str(endDate) + "', "


			if rent == None:
				query = query + "rent=" + str(listing.rent) + ", "
			else:
				query = query + "rent=" + str(rent) + ", "


			if bedrooms == None:
				query = query + "bedrooms=" + str(listing.bedrooms) + ", "
			else:
				query = query + "bedrooms=" + str(bedrooms) + ", "


			if bathrooms == None:
				query = query + "bathrooms=" + str(listing.bathrooms) + ", "
			else:
				query = query + "bathrooms=" + str(bathrooms) + ", "


			if sqft == None:
				query = query + "SqFt=" + str(listing.sqft) + ", "
			else:
				query = query + "SqFt=" + str(sqft) + ", "


			if isApartment == None:
				query = query + "isApartment=" + str(listing.isApartment) + ", "
			else:
				query = query + "isApartment=" + str(isApartment) + ", "


			if website == None:
				query = query + "website='" + str(listing.website) + "', "
			else:
				query = query + "website='" + str(website) + "', "


			if comments == None:
				query = query + "comments='" + str(listing.comments) + "', "
			else:
				query = query + "comments='" + str(comments) + "', "

			# Add a where clause to make sure the correct address is updated			
			query = query + " WHERE address='" + rAddr + "';"

			# Execute actual SQL command to edit the row in the database
			Listing.objects.raw(query)


	# Use a connection cursor to execute an insert statement and add a new listing to the database
	def add_listing(self, address, user, startDate, endDate, rent, bedrooms, bathrooms, sqft, isApartment, website, comments):
		
		with connection.cursor() as cursor:
			# This python module will automatically protect us from SQL injections by encoding the query
			cursor.execute("INSERT INTO Listings_listing (address, startDate, endDate, rent, bedrooms, bathrooms, sqft, isApartment, website, comments, lister_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", [address, startDate, endDate, rent, bedrooms, bathrooms, sqft, isApartment, website, comments, user.id]) 

	def delete_listing(self, listing):
		addr = listing.address

		with connection.cursor() as cursor:
			cursor.execute("DELETE FROM Listings_listing WHERE address=%s;", [addr])

	
	def filter_listings(self, minBedrooms, minBathrooms, maxRent, minSqft, isApartment):
		beds = minBedrooms
		baths = minBathrooms
		rent = maxRent
		sqft = minSqft
		apt = isApartment


		# If the user specifies the type of listing (i.e. apartment or house), only those types of listings are searched for
		with connection.cursor() as cursor:
			if isApartment == -1:
				cursor.execute("SELECT * FROM Listings_listing WHERE bedrooms >= %s AND bathrooms >= %s AND rent <= %s AND sqft >= %s", [beds, baths, rent, sqft])
				listings = cursor.fetchall()
			# If the user doesn't specify, then all listings meeting the other params are returned
			else:
				cursor.execute("SELECT * FROM Listings_listing WHERE bedrooms >= %s AND bathrooms >= %s AND rent <= %s AND sqft >= %s AND isApartment = %s", [beds, baths, rent, sqft, apt])
				listings = cursor.fetchall()

		return listings


	def get_all_listings(self):
		query = "SELECT * FROM Listings_listing"
		return Listing.objects.raw(query)
