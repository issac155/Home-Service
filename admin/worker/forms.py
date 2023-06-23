from django import forms
from.models import Location
from.models import Customer

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'place', 'contact']

