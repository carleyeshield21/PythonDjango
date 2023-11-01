from django.shortcuts import render

# Create your views here.
def hindex(request):
    return render('hindex.html')
