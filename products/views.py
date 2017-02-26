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



    return render(request, 'products_index.html', {'product_list': product_list,})

def add_product(request):


    if request.method == 'POST':
        name = request.POST.get('name')
        products = Product.objects.get(pk=name)
        form = ProductForm(request.POST, instance=products)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/')

    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

