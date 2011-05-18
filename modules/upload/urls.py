# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include
from django.conf import settings
from sitemanager.sites import site
from views import upload_img

def get_urls():
    urlpatterns = patterns('', url(r'^upload/image/$', site.with_perms(upload_img)));
    return urlpatterns
