from django.shortcuts import render
from forms import AplikasyonForm #this module must be created inside the apply_ka_work folder inside the forms.py file

# Create your views here.
def hindex(requester):
    if requester.method == 'POST':
        form = AplikasyonForm()
    return render(requester,'index.html')
    # return render(requester,'hindex.html')
