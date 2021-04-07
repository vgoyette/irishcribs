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
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from home import views as home_view
from Users import views as user_views
from Listings import views as listing_views

urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/signup/', user_views.signup, name='signup'),
    path('accounts/login/', user_views.login, name='login'),
    
    path('userAccount/', user_views.accountPage, name='user_account'),

	path('listings/', listing_views.show_listings, name='show_listings.html'),

    path('admin/', admin.site.urls),


	path('', home_view.home, name='home'),
	path('home/', home_view.home, name='home')
]
