from django import forms
from django.forms import ModelForm, TextInput, Select
from .models import *

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','category']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control textinput', 'placeholder': 'product name', 'type':'text', 'name': 'name'}),
            'category': Select(attrs={'class': 'form-control selectpicker', 'name':'category',})
        }

    new_category = forms.CharField(max_length=64, required=False, label='New Category',
                                   widget=TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'product name', 'type':'text',}
                                   ))

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args,**kwargs)
        self.fields['category'].required = False

    def clean(self):
        cleaned_data = super(ProductForm, self).clean()
        name = self.cleaned_data['name']
        category = self.cleaned_data.get('category')
        new_category = self.cleaned_data.get('new_category')
        if not category and not new_category:
            raise forms.ValidationError('Must specify existing category or new category')
        elif not category:
            category, created = Category.objects.get_or_create(name=new_category)
            self.cleaned_data['category'] = category




