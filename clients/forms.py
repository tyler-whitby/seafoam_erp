from django import forms
from django.forms import ModelForm, widgets, inlineformset_factory
from clients import models
from address.forms import AddressWidget, AddressField


class ClientForm(ModelForm):
    class Meta:
        model = models.Client
        fields = [
            'first_name',
            'last_name',
        ]

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args,**kwargs)



ClientPhoneForm = inlineformset_factory(models.Client,models.PhoneNumber, fields=('phone_type','phone_number',))