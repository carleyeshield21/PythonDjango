from django import forms

class AplikasyonForm(forms.Form): #model for AplikasyonForm, pattern copied from models.py
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    trabaho = models.CharField(max_length=80)
