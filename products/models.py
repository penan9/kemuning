from django.db import models


class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.FloatField()
	price2 = models.FloatField(default='0.0')
	stock = models.IntegerField()
	unit = models.CharField(max_length=10, default='brls')
	image_url = models.CharField(max_length=2083)


class Fuel(models.Model):
	name = models.CharField(max_length=255)
	price = models.FloatField()
	price2 = models.FloatField(default='0.0')
	stock = models.IntegerField()
	unit = models.CharField(max_length=10, default='brls')
	image_url = models.CharField(max_length=2083)
	photo = models.ImageField(upload_to='images/products',null=True)


class Offer(models.Model):
	code = models.CharField(max_length=10)
	description = models.CharField(max_length=255)
	discount = models.FloatField()
	mode = models.CharField(max_length=255)
