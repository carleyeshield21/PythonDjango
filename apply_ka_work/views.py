from django.shortcuts import render
from .forms import AplikasyonForm #this module must be created inside the apply_ka_work folder inside the forms.py file, we have to add the dot at
# the beginning of the forms module because we are importing the forms in the same folder directory
from .models import Forma

# Create your views here.
def hindex(requester): #this function is used to retrieve the input that the user will provide in the page
    if requester.method == 'POST':
        form = AplikasyonForm(requester.POST)
        if form.is_valid(): #validate the form first
            firstname = form.cleaned_data['first_name'] #argument should be the variable in the index.html name of the input
            lastname = form.cleaned_data['lust_name'] #argument should be the variable in the index.html name of the input
            email = form.cleaned_data['email'] #argument should be the variable in the index.html name of the input
            occupation = form.cleaned_data['occupation'] #argument should be the variable in the index.html name of the input
            print(firstname, lastname, email, occupation)
    return render(requester,'index.html')
    # return render(requester,'hindex.html')
