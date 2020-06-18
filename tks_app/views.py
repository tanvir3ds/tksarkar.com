from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from . models import Interviews

# Create your views here.
def home(request):
    
    return render(request, "home.html")

def profile(request):

    return render(request, "profile.html")



def awards(request):

    return render(request, "awards.html")

def interviews(request):
    interviews= Interviews.objects.all()
    

    return render(request, "interviews.html",{
        'interviews' : interviews,
    
    })



def blog(request):

    return render(request, "blog.html")

def photos(request):

    return render(request, "photos.html")

    
    
    
    