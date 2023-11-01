from django.shortcuts import render

# Create your views here.
def hindex(requester):
    if requester.method == 'POST':
        
    return render(requester,'index.html')
    # return render(requester,'hindex.html')
