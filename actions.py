"""
Custom do_complete actions
"""
from six.moves.urllib_parse import quote
from django.urls import reverse
from social_core.utils import user_is_authenticated, setting_url

def do_merchant_complete(backend, user=None, redirect_name='next', *args, **kwargs):
    data = backend.strategy.request_data()
    is_authenticated = user_is_authenticated(user)
    user = user if is_authenticated else None
    user = backend.complete(user=user, *args, **kwargs)
    # pop redirect value before the session is trashed on login(), but after
    # the pipeline so that the pipeline can change the redirect if needed
    redirect_value = backend.strategy.session_get(redirect_name, '') or \
                     data.get(redirect_name, '')
    url = setting_url(backend, reverse(backend.setting('MERCHANT_REDIRECT_FIELDNAME')))
    if redirect_value and redirect_value != url:
        redirect_value = quote(redirect_value)
        url += ('&' if '?' in url else '?') + \
               '{0}={1}'.format(redirect_name, redirect_value)
    return backend.strategy.redirect(url)