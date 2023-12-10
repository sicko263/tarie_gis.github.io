from django.forms import TextInput, Field
from django_select2 import forms as s2forms
from django import forms
from .models import *
from django.forms import DateInput

class farms_allocationForm(forms.ModelForm):
    class Meta:
        model = farms_allocation
        fields = "__all__"
        exclude = ('date_created','date_updated')

        widgets = {
            'maize': forms.NumberInput(attrs={'class':'form-control'}),
            'fertilizer': forms.NumberInput(attrs={'class':'form-control'}),
            'sorghum': forms.TextInput(attrs={'class':'form-control'}),
            'farms': forms.Select(attrs={'class':'form-control'}),
        }