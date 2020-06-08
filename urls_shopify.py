"""URLs module"""
from django.conf import settings
from django.conf.urls import url

from social_core.utils import setting_name
from . import views


extra = getattr(settings, setting_name('TRAILING_SLASH'), True) and '/' or ''

app_name = 'ecommerce_shopify'

urlpatterns = [
    # authentication
    url(r'^auth/(?P<backend>[^/]+){0}$'.format(extra), views.shopify_auth,
        name='shopify_auth'),
    url(r'^complete/(?P<backend>[^/]+){0}$'.format(extra), views.shopify_complete,
        name='shopify_complete'),
]
