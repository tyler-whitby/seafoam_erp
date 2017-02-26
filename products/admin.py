from django.contrib import admin
from django.apps import apps
from .models import *

# Register your models here.

#admin.site.register(.models)

for model in apps.get_app_config('products').models.values():
    admin.site.register(model)