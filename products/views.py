from django.shortcuts import render
from django.template import Context, Template, loader
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, "products_index.html", context)
