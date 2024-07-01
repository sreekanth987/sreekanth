from django import forms
from.models import *

# events=[('WEDDING','WEDDING'),('BAPTISM','STAGE EVENTS'),('PERIDAL','BRITHDAY'),('FAMILY GETTOGETHER','OTHERS'),]
class nform(forms.Form):
    clintname = forms.CharField(max_length=300)
    phone = forms.IntegerField()
    email = forms.CharField()
    eventname = forms.CharField(max_length=500)
    date_from=forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),input_formats=['%Y-%m-%d', '%m/%d/%Y'])
    date_to=forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),input_formats=['%Y-%m-%d', '%m/%d/%Y'])


class model_form(forms.ModelForm):
    class Meta:
        model=newevent
        fields='__all__'

class new_form(forms.ModelForm):
    class Meta:
        model=register
        fields='__all__'


