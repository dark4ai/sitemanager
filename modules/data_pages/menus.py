from django.conf import settings
from sitemanager.sites import site
from sitemanager.menus import Menu, manager_menu
from urls import morfology_pages, list_pages

def setmenu():
    for p, urlname, forms, numerals in settings.DATA_PAGES:
        morfology_pages[urlname] = (forms, numerals)
        list_pages.append(urlname)
        manager_menu.append(Menu("datapage_" + urlname, p, "/admin/data_pages/%s/pages/" % urlname))
