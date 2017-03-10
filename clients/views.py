from django.shortcuts import render
from django.template import Context, Template, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import *
from .models import *

# Create your views here.

def clients_index(request):
    form = ClientForm()
    form_error = None




    return render(request, 'clients/clients_index.html', {'form': form, 'form_error': form_error})

def add_client(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        products = Client.objects.get(pk=name)
        form = ClientForm(request.POST, instance=products)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/')

    else:
        form = ClientForm()
    return render(request, 'products/add_product.html', {'form': form})