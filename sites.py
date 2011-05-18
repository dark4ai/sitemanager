# -*- coding: utf-8 -*-
import re
from django import http, template
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.db.models.base import ModelBase
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.utils.functional import update_wrapper
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy, ugettext as _
from django.utils.importlib import import_module
from django.views.decorators.cache import never_cache
from django.conf import settings
from context_processors import manager_consts
from sitemanager import menus

ERROR_MESSAGE = ugettext_lazy("Please enter a correct username and password. Note that both fields are case-sensitive.")
LOGIN_FORM_KEY = 'this_is_the_login_form'

class SiteManager(object):
    def __init__(self):
       self.modules = []

    def index(self, request):
        if menus.index_redirect:
            return HttpResponseRedirect(menus.index_redirect)
        context_instance = template.RequestContext(request, processors=[manager_consts])
        return render_to_response('cms/index.html', {}, context_instance=context_instance)


    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff

    def display_login_form(self, request, error_message=''):
        request.session.set_test_cookie()
        context = {
            'app_path': request.get_full_path(),
            'error_message': error_message,
        }
        context_instance = template.RequestContext(request)
        return render_to_response('cms/login.html', context,
            context_instance=context_instance)

    def login(self, request):
        from django.contrib.auth.models import User

        # If this isn't already the login page, display it.
        if not request.POST.has_key(LOGIN_FORM_KEY):
            if request.POST:
                message = _("Please log in again, because your session has expired.")
            else:
                message = ""
            return self.display_login_form(request, message)

        # Check that the user accepts cookies.
        if not request.session.test_cookie_worked():
            message = _("Looks like your browser isn't configured to accept cookies. Please enable cookies, reload this page, and try again.")
            return self.display_login_form(request, message)
        else:
            request.session.delete_test_cookie()

        # Check the password.
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is None:
            return self.display_login_form(request, ERROR_MESSAGE)

        # The user data is correct; log in the user in and continue.
        else:
            if user.is_active and user.is_staff:
                login(request, user)
                return http.HttpResponseRedirect(request.get_full_path())
            else:
                return self.display_login_form(request, ERROR_MESSAGE)
    login = never_cache(login)

    def logout(self, request):
        from django.contrib.auth.views import logout
        defaults = {}
        return logout(request, settings.SITE_ADRESS)
    logout = never_cache(logout)

    def with_perms(self, view, cacheable=False):
        def inner(request, *args, **kwargs):
            if not self.has_permission(request):
                return self.login(request)
            return view(request, *args, **kwargs)
        if not cacheable:
            inner = never_cache(inner)
        if not getattr(view, 'csrf_exempt', False):
            inner = csrf_protect(inner)
        return update_wrapper(inner, view)

    def get_urls(self):
        from django.conf.urls.defaults import patterns, url, include
        urlpatterns = patterns('',
            url(r'^$',
                self.with_perms(self.index),
                name='index'),
            url(r'^logout/$',
                self.with_perms(self.logout),
                name='logout'),
        )
        for module in self.modules:
            urlpatterns += module.get_urls()
        return urlpatterns

    def urls(self):
        return self.get_urls()
    urls = property(urls)


site = SiteManager()
