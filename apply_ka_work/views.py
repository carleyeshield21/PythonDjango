from django.shortcuts import render
from forms import AplikasyonForm

# Create your views here.
def hindex(requester):
    if requester.method == 'POST':
        form = AplikasyonForm()
    return render(requester,'index.html')
    # return render(requester,'hindex.html')
