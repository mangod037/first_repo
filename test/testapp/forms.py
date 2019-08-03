from django import forms
from .models import AllServices

class AllServicesForm(forms.ModelForm):
    class Meta:
        model = AllServices
        fields = ('engName', 'company', 'price')