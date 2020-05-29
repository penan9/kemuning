from django.contrib import admin
from .models import Product, Offer, Fuel


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price', 'price2', 'unit')


class FuelAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price', 'price2', 'unit', 'photo')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Fuel, FuelAdmin)
admin.site.register(Offer, OfferAdmin)
