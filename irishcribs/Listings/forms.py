from django import forms

class AddForm(forms.Form):
    address = forms.CharField(label='Address', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    startDate = forms.DateField(label='Start Date (mm/dd/yyyy)', required=False,  widget=forms.TextInput(attrs={'placeholder': 'MM-DD-YYYY'}))
    endDate = forms.DateField(label='End Date (mm/dd/yyyy)', required=False, widget=forms.TextInput(attrs={'placeholder': 'MM-DD-YYYY'}))
    rent = forms.FloatField(label='Rent ($/Month)', required=False,  widget=forms.TextInput(attrs={'placeholder': 'Rent'}))
    bedrooms = forms.FloatField(label='# of Bedrooms', required=False,  widget=forms.TextInput(attrs={'placeholder': '# of Bedrooms'}))
    bathrooms = forms.FloatField(label='# of Bathrooms', required=False,  widget=forms.TextInput(attrs={'placeholder': '# of Bathrooms'}))
    sqft = forms.FloatField(label='Square Footage', required=False,  widget=forms.TextInput(attrs={'placeholder': 'Square Footage'}))
    isApartment = forms.IntegerField(label='Apartment?', required=False,  widget=forms.TextInput(attrs={'placeholder': 'Enter 1 if it is an apartment, 0 for non-apartments'}))
    website = forms.CharField(label='Link to website', required=False,  max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Website Link (Or Email to Contact You)'}))
    comments = forms.CharField(label='Any other comments', required=False,  max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Leave any other comments about the property here'}))

class EditForm(forms.Form):
    startDate = forms.DateField(label='Start Date (mm/dd/yyyy)', required=False, widget=forms.TextInput(attrs={'placeholder': 'MM-DD-YYYY'}))
    endDate = forms.DateField(label='End Date (mm/dd/yyyy)', required=False,  widget=forms.TextInput(attrs={'placeholder': 'MM-DD-YYYY'}))
    rent = forms.FloatField(label='Rent ($/Month)', required=False,  widget=forms.TextInput(attrs={'placeholder': 'Rent'}))
    bedrooms = forms.FloatField(label='# of Bedrooms', required=False,  widget=forms.TextInput(attrs={'placeholder': '# of Bedrooms'}))
    bathrooms = forms.FloatField(label='# of Bathrooms', required=False,  widget=forms.TextInput(attrs={'placeholder': '# of Bathrooms'}))
    sqft = forms.FloatField(label='Square Footage', required=False,  widget=forms.TextInput(attrs={'placeholder': 'Square Footage'}))
    isApartment = forms.IntegerField(label='Apartment?', required=False,  widget=forms.TextInput(attrs={'placeholder': 'Enter 1 if it is an apartment, 0 for non-apartments'}))
    website = forms.CharField(label='Link to website', required=False,  max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Website Link (Or Email to Contact You)'}))
    comments = forms.CharField(label='Any other comments', required=False,  max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Leave any other comments about the property here'}))

class FilterForm(forms.Form):
    bedrooms = forms.FloatField(label='Minimum # of Bedrooms', required=False, widget=forms.TextInput(attrs={'placeholder': '# of Bedrooms'}))
    bathrooms = forms.FloatField(label='Minimum # of Bathrooms', required=False, widget=forms.TextInput(attrs={'placeholder': '# of Bathrooms'}))
    sqft = forms.FloatField(label='Minimum Square Footage', required=False, widget=forms.TextInput(attrs={'placeholder': 'Square Footage'}))
    rent = forms.FloatField(label='Maximum Rent ($/Month)', required=False, widget=forms.TextInput(attrs={'placeholder': 'Rent'}))
    isApartment = forms.IntegerField(label='Apartment?', required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter 1 for apartments, 0 for non-apartments, or leave blank to see all'}))
