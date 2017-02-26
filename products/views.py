from django.shortcuts import render
from django.template import Context, Template, loader
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *


from django_datatables_view.base_datatable_view import BaseDatatableView

# Create your views here.


def products_list(request):
    product_list = [product for product in Product.objects.all()]
    return render(request, 'products_index.html', {'product_list': product_list})






