# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include
from sitemanager.sites import SiteManager, site
from sitemanager.menus import Menu, manager_menu
from views import test

def get_urls():
    from django.conf.urls.defaults import patterns, url, include
    urlpatterns = patterns('',
        url(r'^testmodule/$', site.with_perms(test)),
    )
    return urlpatterns

manager_menu.append(Menu("testlink", "Тестовый модуль", "/admin/testmodule/"));
