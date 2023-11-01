from django.shortcuts import render

# Create your views here.
def hindex(requester):
    return render(requester,'hindex.html')
