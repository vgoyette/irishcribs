"""irishcribs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, register_converter
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import converts

from home import views as home_view
from Users import views as user_views
from Listings import views as listing_views
from Listings.views import EditListingView, DeleteListingView

from Sublets import views as sublet_views
from Sublets.views import EditSubletView, DeleteSubletView

register_converter(converts.FloatUrlParameterConverter, 'float')

urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/signup/', user_views.signup, name='signup'),
    path('accounts/login/', user_views.login, name='login'),
    path('userAccount/', user_views.accountPage, name='user_account'),

	path('listings/', listing_views.view_listings, name='show_listing'),
    path('addlisting/', listing_views.add_listings, name='add_listing'),
    path('editlisting/<pk>/', EditListingView.as_view(), name='edit_listing'),
    path('deletelisting/<pk>/', DeleteListingView.as_view(), name='delete_listing'),
    #path('deleteListing/', listing_views.delete_listing, name='delete_listing'),
    path('filterListings/', listing_views.filter_listing_form, name='filter_listing_form'),
    #path('filteredListings/<float:bedrooms>/<float:bathrooms>/<float:rent>/<float:sqft>/<float:isApartment>/', listing_views.show_filtered_listings, name='filtered'),
    path('filteredListings/', listing_views.filtered_listings, name='filtered_listings'),
	path('messages/', include('django_messages.urls')),
	path('sublets/', sublet_views.view_sublets, name='show_sublet'),
    path('addsublet/', sublet_views.add_sublets, name='add_sublet'),
    path('editsublet/<pk>/', EditSubletView.as_view(), name='edit_sublet'),
    path('deletesublet/<pk>/', DeleteSubletView.as_view(), name='delete_sublet'),
    path('filtersublets/', sublet_views.filter_sublet_form, name='filter_sublet_form'),
    path('filteredsublets/', sublet_views.filtered_sublets, name='filtered_sublets'),
    path('admin/', admin.site.urls),


	path('', home_view.home, name='home'),
	path('home/', home_view.home, name='home')
]
