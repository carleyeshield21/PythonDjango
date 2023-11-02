from django import forms

class AplikasyonForm(forms.Form): #model for AplikasyonForm, pattern copied from forms.py, then change models to forms
    firstname = forms.CharField(max_length=80,required=True)
    lastname = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    trabaho = forms.CharField(max_length=80)
