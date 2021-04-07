from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.

class Listing(models.Model):
	address = models.CharField(max_length=100, default='1 Compton Family Ice Arena, Notre Dame, IN 46556')
	bedrooms = models.FloatField(default=0)
	bathrooms = models.FloatField(default=0)
	rent = models.FloatField(default=0)
	sqft = models.FloatField(default=0)
	uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	
	def __str__(self):
		return str(self.uuid)


class listing_library():
	
	def edit_listing(listing=None, address="", bedrooms=-1, bathrooms=-1, rent=-1):
		# 0 is house, 1 is apartment

		# Build query for an update
		query = "UPDATE table_name SET "

		if listing is not None:

			if address == "":
				query = query + "address = '" + str(listing.address) + "', "
			else:
				query = query + "address = '" + str(address) + "', "


			if bedrooms == -1:
				query = query + "bedrooms = " + str(listing.bedrooms) + ", "
			else:
				query = query + "bedrooms = " + str(bedrooms) + ", "


			if bathrooms == -1:
				query = query + "bathrooms = " + str(listing.bathrooms) + ", "
			else:
				query = query + "bathrooms = " + str(bathrooms) + ", "


			if rent != -1:
				query = query + "rent = " + str(listing.rent)
			else:
				query = query + "rent = " + rent

			listing_uuid = listing.uuid

			query = query + "WHERE uuid=" + listing.uuid




