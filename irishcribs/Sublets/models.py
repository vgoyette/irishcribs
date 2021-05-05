from django.db import models

# Create your models here.
#!/usr/bin/python3
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import connection
import mysql.connector
import uuid

# Create your models here.

cnx = mysql.connector.connect(user='djangouser', password='pw', database='Listings')
cursor = cnx.cursor()

class Sublet(models.Model):
	sublet_lister = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=100, primary_key=True)
	startDate = models.DateField(blank=True, null=True)
	endDate = models.DateField(blank=True, null=True)
	rent = models.FloatField(blank=True, null=True)
	bedrooms = models.FloatField(blank=True, null=True)
	bathrooms = models.FloatField(blank=True, null=True)
	sqft = models.FloatField(blank=True, null=True)
	isApartment = models.IntegerField(blank=True, null=True)
	website = models.CharField(max_length=100, blank=True, null=True)
	comments = models.CharField(max_length=100, blank=True, null=True)
	
	def __str__(self):
		return str(self.address)


# This library is just so that we don't have to make SQL calls in our views functions
# The views functions are already substantially complex, so using this library
# will clean things up in those functions
class sublet_library():
	
	# This is the beefiest function in the library, but it's just because 
	# we have to check which features the user wants to edit.
	# Once that's done, we just do an UPDATE statement to make the changes
	def edit_sublet(self, listing=None, address=None, startDate=None, endDate=None, rent=None, bedrooms=None, bathrooms=None, sqft=None, isApartment=None, website=None, comments=None):
		# 0 is house, 1 is apartment

		
		if sublet is not None:
			# We want to make the default query value the original sublet's values
			# i.e. if a user only wanted to edit the rent, they could only fill in that
			# field, and we would only set a new value for the rent column
			# All of the other columns would be "updated" with their original value,
			# so it's not really updating those ones
			new_address     = sublet.address
			new_startDate   = sublet.startDate
			new_endDate     = sublet.endDate
			new_rent        = sublet.rent
			new_bedrooms    = sublet.bedrooms
			new_bathrooms   = sublet.bathrooms
			new_sqft        = sublet.sqft
			new_isApartment = sublet.isApartment
			new_website     = sublet.website
			new_comments    = sublet.comments

			if address is not None:
				new_address = address

			if startDate is not None:
				new_startDate = startDate
			
			if endDate is not None:
				new_endDate = endDate

			if rent is not None:
				new_rent = rent

			if bedrooms is not None:
				new_bedoomrs = bedrooms

			if bathrooms is not None:
				new_bathrooms = bathrooms

			if sqft is not None:
				new_sqft = sqft

			if isApartment is not None:
				new_isApartment = isApartment

			if website is not None:
				new_website = website

			if comments is not None:
				new_comments = comments

			# Add a where clause to make sure the correct address is updated			
			query = query + " WHERE address='" + rAddr + "';"

			# Execute actual SQL command to edit the row in the database
			with connection.cursor() as cursor:
				cursor.execute("""UPDATE Sublets_sublet 
								  SET address=%s, 
								      startDate=%s, 
									  endDate=%s, 
									  rent=%s, 
									  bedrooms=%s, 
									  bathrooms=%s, 
									  sqft=%s,
									  isApartment=%s,
									  website=%s,
									  comments=%s""",
								[new_address, new_startDate, new_endDate, new_rent, 
								 new_bedrooms, new_bathrooms, new_sqft, new_isApartment,
								 new_website, new_comments]
							  )


	# Use a connection cursor to execute an insert statement and add a new listing to the database
	def add_sublet(self, address, user, startDate, endDate, rent, bedrooms, bathrooms, sqft, isApartment, website, comments):
		
		with connection.cursor() as cursor:
			# This python module will automatically protect us from SQL injections by encoding the query
			cursor.execute("""INSERT INTO Sublets_sublet 
								(address, 
								startDate, 
								endDate, 
								rent, 
								bedrooms, 
								bathrooms, 
								sqft, 
								isApartment, 
								website, 
								comments, 
								sublet_lister_id) 
							  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", 
							  [address, startDate, endDate, rent, bedrooms, bathrooms, sqft, isApartment, website, comments, user.id])

			
	# Build a query to delete a specified sublet
	def delete_sublet(self, sublet):
		addr = sublet.address
		with connection.cursor() as cursor:
			cursor.execute("DELETE FROM Sublets_sublet WHERE address=%s;", [addr])


	# Build a query to filter sublets by certain criteria
	def filter_sublets(self, minBedrooms, minBathrooms, maxRent, minSqft, isApartment):
		beds = minBedrooms
		baths = minBathrooms
		rent = maxRent
		sqft = minSqft
		apt = isApartment

		# When we try to filter, if we have a null value then the comparison will always be false
		# Here, we make sure that we set the values of each thing we search on to make sure that doesn't happen
		if minBedrooms == None:
			beds = 0
		if minBathrooms == None:
			baths = 0
		if maxRent == None:
			rent = 10000
		if minSqft == None:
			sqft = 0
		if isApartment == None:
			apt = -1


		# If the user specifies the type of listing (i.e. apartment or house), 
		# only those types of listings are searched for
		with connection.cursor() as cursor:
			if apt == -1:
				cursor.execute("""SELECT * FROM Sublets_sublet 
								  WHERE bedrooms >= %s 
								    AND bathrooms >= %s 
									AND rent <= %s 
									AND sqft >= %s""", 
								[beds, baths, rent, sqft])
				sublets = cursor.fetchall()
			# If the user doesn't specify, then all listings meeting the other params are returned
			else:
				cursor.execute("""SELECT * FROM Sublets_sublet 
								  WHERE bedrooms >= %s 
									AND bathrooms >= %s 
									AND rent <= %s 
									AND sqft >= %s 
									AND isApartment = %s""", 
								[beds, baths, rent, sqft, apt])
				sublets = cursor.fetchall()

		return sublets


	# Use a query to get all of the sublets in the database
	def get_all_sublets(self):
		# SELECT statements can be done much more easily than other queries
		# using the Model.objects.raw() function
		query = "SELECT * FROM Sublets_sublet"
		return Sublet.objects.raw(query)
