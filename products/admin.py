from django.contrib import admin
from .models import Offer, Product


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'stock', 'price', 'price2', 'unit', 'photo', 'button_name', 'youtube_id')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
