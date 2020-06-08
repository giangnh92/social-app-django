"""URLs module"""
from django.conf import settings
from django.conf.urls import url
from django.urls import path

from social_core.utils import setting_name
from . import views


extra = getattr(settings, setting_name('TRAILING_SLASH'), True) and '/' or ''

app_name = 'social_merchant'

urlpatterns = [
    url(r'auth/(?P<backend>[^/]+){0}$'.format(extra), views.merchant_auth, name='merchant_auth'),
    url(r'complete/(?P<backend>[^/]+){0}$'.format(extra), views.merchant_complete, name='merchant_complete')
]