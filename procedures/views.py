from django.shortcuts import render
from .models import Procedure

def procedure_list(request):
    procedures = Procedure.objects.all().order_by('date');
    return render(request, 'procedure/procedure_list.html', { 'procedures': procedures })
