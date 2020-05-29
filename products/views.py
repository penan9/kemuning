from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Fuel

def index(request):
	fuels = Fuel.objects.all()
	return render(request,'index_fuel.html', {'fuels':fuels})


def index_products(request):
	products = Product.objects.all()
	return render(request,'index1.html', {'products':products})


def new(request):
	return HttpResponse('New products')


def sales(request):
	return HttpResponse('Products on sales!')


def details(request):
	return HttpResponse('Products details ...')
