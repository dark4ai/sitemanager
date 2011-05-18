# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include
from sitemanager.sites import SiteManager, site
from views import pages, page, delete_page

def get_urls():
    urlpatterns = patterns('', url(r'/([\w_]+)/page/(\d+)/$', site.with_perms(page)))
    urlpatterns += patterns('', url(r'/([\w_]+)/page/$', site.with_perms(page)))
    urlpatterns += patterns('', url(r'/([\w_]+)/pages/$', site.with_perms(pages)))
    urlpatterns += patterns('', url(r'/delete_page/(\d+)/$', site.with_perms(delete_page)))
    return urlpatterns

morfology_pages = {}
list_pages = []
