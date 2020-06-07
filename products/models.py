import os
from django.db import models
from procedures.models import Procedure
from django.dispatch import receiver


class Product(models.Model):
	name = models.CharField(max_length=255)
	code = models.ForeignKey(Procedure, default='1', verbose_name='Procedure', null=True, blank=True, on_delete=models.SET_NULL)
	code2 = models.CharField(max_length=10, default="")
	price = models.FloatField()
	price2 = models.FloatField(default='0.0')
	stock = models.IntegerField()
	unit = models.CharField(max_length=100, default='brls')
	youtube_id = models.CharField(max_length=100, default='', blank=True)
	button_name = models.CharField(max_length=100, default='procedure')
	photo = models.ImageField(upload_to='images/products', blank=True, default='')


class Offer(models.Model):
	code = models.CharField(max_length=10)
	description = models.CharField(max_length=255)
	discount = models.FloatField()
	mode = models.CharField(max_length=255)


@receiver(models.signals.post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    print ("post delete ... ")
    print (sender)
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


@receiver(models.signals.pre_save, sender=Product)
def auto_delete_file_on_change(sender, instance, **kwargs):
    print ("pre save ... ")
    print (sender)
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).photo
    except sender.DoesNotExist:
        return False

    new_file = instance.photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
