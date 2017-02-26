from django.shortcuts import render
from django.template import Context, Template, loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    template = loader.get_template("products_base.html")
    return render(request, "products_base.html")
