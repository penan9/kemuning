from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
import random
from aboutus.views import get_image

def index(request):
        products = Product.objects.all().order_by('date')
        last_entry = Product.objects.latest("date")
        last_date = last_entry.date
        for product in products:
            code = str(product.code)[0:4]
            if code != product.code2:
               product.code2 = code
               product.save()
        image1 = get_image("home")
        return render(request,'product.html', {'last_date': last_date, 'products':products, 'image1':image1})


def new(request):
        products = Product.objects.all()
        homepage = "welcome: "
        for product in products:
            code = str(product.code)[0:4]
            if code != product.code2:
               product.code2 = code
               product.save()
            homepage += product.code2
            homepage += " : "
            homepage += str(product.code)
            homepage += " ; "
        return HttpResponse('New products ' + homepage)


def sales(request):
	return HttpResponse('Products on sales!')


def details(request):
	return HttpResponse('Products details ...')
