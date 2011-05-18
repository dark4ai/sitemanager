# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include
from sitemanager.sites import SiteManager, site
from views import support


def get_urls():
    from django.conf.urls.defaults import patterns, url, include
    urlpatterns = patterns('',
        url(r'^support/$', site.with_perms(support)),
        url(r'^support/success/$', site.with_perms(support), {"form_status":True}),
    )
    return urlpatterns
