from django.shortcuts import render
from forms import AplikasyonForm #this module must be created inside the apply_ka_work folder inside the forms.py file

# Create your views here.
def hindex(requester):
    if requester.method == 'POST':
        form = AplikasyonForm()
        firstname = form.cleaned_data['first_name'] #argument should be the variable in the index.html name of the input
        lastname = form.cleaned_data['lust_name'] #argument should be the variable in the index.html name of the input
        email = form.cleaned_data['email'] #argument should be the variable in the index.html name of the input
    return render(requester,'index.html')
    # return render(requester,'hindex.html')
