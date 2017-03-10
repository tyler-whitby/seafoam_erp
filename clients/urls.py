from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', ClientsIndexView.as_view(), name='clients_index'),

]