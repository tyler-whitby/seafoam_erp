from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from account import views as acc_views

from products import urls


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),

    url(r"^products/", include('products.urls', namespace="products")),

    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/login/$", acc_views.LoginView.as_view(template_name="login.html"), name='account_login'),
    url(r"^account/logout/$", acc_views.LogoutView.as_view(template_name="logout.html"), name='account_logout'),

    url(r"^account/", include("account.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
