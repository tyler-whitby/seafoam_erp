#stronghold new mware class
from django.utils.deprecation import MiddlewareMixin
from stronghold.middleware import LoginRequiredMiddleware


#create middleware class with mixin to fit new middleware standard
class SiteLoginRequiredMiddleware(MiddlewareMixin, LoginRequiredMiddleware):
    pass