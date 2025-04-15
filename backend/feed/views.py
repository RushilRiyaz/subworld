from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return render(request, 'feed/home.html')

def about(request):
    return render(request, 'feed/about.html', {'title': 'About Page'})
