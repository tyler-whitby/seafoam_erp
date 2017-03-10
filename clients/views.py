from django.shortcuts import render
from django.template import Context, Template, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from .forms import *
from .models import *

# Create your views here.

class ClientsIndexView(CreateView):
    template_name = 'products/products_index.html'
    form_class = ClientForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        phone_form = ClientPhoneForm()

        return self.render_to_response(
            self.get_context_data(forms=form,
                                  phone_form=phone_form)
        )

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