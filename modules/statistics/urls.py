# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include
from sitemanager.sites import SiteManager, site
from views import statistics, ya_api

def get_urls():
    from django.conf.urls.defaults import patterns, url, include
    urlpatterns = patterns('',
        url(r'^statistics/$', site.with_perms(statistics)),
        url(r'^statistics/ya_api/(week|month|year)/$', site.with_perms(ya_api)),
    )
    return urlpatterns
