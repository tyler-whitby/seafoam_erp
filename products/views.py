from django.shortcuts import render
from django.template import Context, Template, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import *
from .forms import *

from django_datatables_view.base_datatable_view import BaseDatatableView


# Create your views here.


def products_list(request):
    product_list = [product for product in Product.objects.all()]

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/')

        else:
            form_error = 'invalid_form'
    else:
        form = ProductForm()
        form_error = 'none'


    return render(request, 'products/products_index.html', {'product_list': product_list, 'form':form, 'form_error':form_error})

def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/')

    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

