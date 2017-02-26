from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', products_list, name='product_list'),

]