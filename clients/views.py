from django.shortcuts import render
from django.template import Context, Template, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, View
from .forms import *
from .models import *

# Create your views here.

class ClientsIndexView(CreateView):
    template_name = 'clients/clients_index.html'
    form_class = NewClientForm
    success_url = '/'


    def get(self, request, *args, **kwargs):
        client_list = Client.objects.all()

        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  client_list=client_list,
                                  )
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        newclientform = NewClientForm(self.request.POST)
        if newclientform.is_valid():
            return self.form_valid(newclientform)
        else:
            return self.form_invalid(newclientform)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/clients')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

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