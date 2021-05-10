from django.shortcuts import render, redirect

# This is the function to actually display the filtered listings to the user
def map_query(request):
    #sublets = request.session['filtered_sublets']

    return render(request, 'map_query.html') #,{'sublets' : sublets})
         
