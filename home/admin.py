from django.contrib import admin
from .models import Home


class HomeAdmin(admin.ModelAdmin):
#    pass
    list_display = ('filename', 'videofile')


# Register your models here.
admin.site.register(Home, HomeAdmin)
