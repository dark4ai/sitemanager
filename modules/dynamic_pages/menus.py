from django.conf import settings
from sitemanager.sites import site
from sitemanager.menus import Menu, manager_menu

def setmenu():
    for page, urlname in settings.DYNAMIC_PAGES:
        manager_menu.append(Menu("dp_" + urlname, page, "/admin/dynamic_pages/%s/" % urlname));
