from django.shortcuts import render,redirect
from django.http  import Http404

# Create your views here.
def intro(request):
    return render(request, 'navbar.html')
