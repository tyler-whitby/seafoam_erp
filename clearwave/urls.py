from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from account import views as acc_views

from products import urls
from clients import urls


urlpatterns = [
    url(r"^grappelli/", include('grappelli.urls')),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^account/login/$", acc_views.LoginView.as_view(template_name="clearwave/login.html"), name='account_login'),
    url(r"^account/logout/$", acc_views.LogoutView.as_view(template_name="clearwave/logout.html"),
        name='account_logout'),
    url(r"^account/signup/$", acc_views.SignupView.as_view(template_name="account/signup.html"), name='signup'),

    url(r"^account/", include("account.urls")),

    url(r"^$", TemplateView.as_view(template_name="clearwave/homepage.html"), name="home"),

    url(r"^products/", include('products.urls', namespace="products")),
    url(r"^clients/", include('clients.urls', namespace='clients')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
