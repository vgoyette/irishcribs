from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_lib():
	def add_user(username, first_name, last_name, password, email):
		temp = User(
				username=username,
				first_name=first_name,
				last_name=last_name,
				password=password,
				email=email
			)

		temp.save()
		return temp
