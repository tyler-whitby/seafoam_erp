from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', clients_index, name='clients_index'),

]