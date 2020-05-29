from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('new', views.new),
	path('sales', views.sales),
	path('details', views.details)
]
