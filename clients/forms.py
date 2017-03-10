from django import forms
from django.forms import ModelForm, widgets, inlineformset_factory
from address.forms import AddressWidget, AddressField
from clients.models import *


class NewClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ['addresses','phones','emails']
        widgets = {
            'company': widgets.Select
        }

    new_company = forms.CharField()
    phone_type = forms.ChoiceField(choices=PhoneNumber.TYPE_OPTIONS)
    phone = forms.CharField()
    email_type = forms.CharField()
    email = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(NewClientForm, self).__init__(*args,**kwargs)
        self.fields['company'].required = False

    def clean(self):
        super(NewClientForm,self).clean()
        company = self.cleaned_data.get('company')
        new_company = self.cleaned_data.get('new_company')
        if not company and not new_company:
            raise forms.ValidationError('Must specify existing category or new category')
        elif not company:
            company, created = Company.objects.get_or_create(company_name=new_company)
            self.cleaned_data['company']= company

        return self.cleaned_data




