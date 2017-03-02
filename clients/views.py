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