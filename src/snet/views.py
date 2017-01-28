from django.views import View
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import sample

def index(request , *args ,**kwargs):
    obj = sample()
    obj.fill("this is my first post","abhishek")
    if request.method == "GET": 
        bg_image = 'https://upload.wikimedia.org/wikipedia/commons/0/05/20100726_Kalamitsi_Beach_Ionian_Sea_Lefkada_island_Greece.jpg'
        context = {
            "title" : "home page",
            "ques" : obj,
            "bg_image" : bg_image
        }
    obj.save()
    return render(request , "home.html" , context)

class home(Vie):
    