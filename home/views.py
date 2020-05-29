from django.http import HttpResponse
from django.shortcuts import render
from .models import Home
import random


def index(request):
    home = Home.objects.all()
    home1 = Home()
    homepage = "welcome: "
    try:
        myhomes = []
        for myhome in home:
            myhomes.append(myhome.filename) 
        home1.filename =random.choice(myhomes) 
    except IndexError:
        homepage += "Error: IndexError" 
        print (homepage)
    else:
        if home1:
            homepage += str(home1.filename)
 #   returnHttpResponse(homepage)
    return render(request, 'index.html', { 'home1': home1})
