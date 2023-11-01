from django import forms

class AplikasyonForm(forms.Form): #model for AplikasyonForm
    firstname = forms.CharField(max_length=80)
