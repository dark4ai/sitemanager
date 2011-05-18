# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include
from django.conf import settings
from sitemanager.sites import SiteManager, site
from views import view_page, save_page

def get_urls():
    urlpatterns = patterns('', url(r'dynamic_pages/save/$', site.with_perms(save_page)));
    for page, urlname in settings.DYNAMIC_PAGES:
        urlpatterns += patterns('', url(r'^dynamic_pages/%s/$' % urlname, site.with_perms(view_page), {'page':page, 'urlname':urlname}))
    return urlpatterns
