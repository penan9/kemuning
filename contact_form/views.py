from django.shortcuts import render
from .models import Contact_Form

def contact_form(request):
    contact_forms = Contact_Form.objects.all().order_by('date');
    return render(request, 'contact_form/contact_form.html', { 'contact_forms': contact_forms })
