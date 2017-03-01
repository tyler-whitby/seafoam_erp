from django.shortcuts import render
from django.template import Context, Template, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

# Create your views here.

def clients_index(request):

    return render(request, 'clients/clients_index.html')