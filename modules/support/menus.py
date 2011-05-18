#-*- coding:utf-8 -*-
from sitemanager import menus
from sitemanager.menus import Menu, manager_menu

def setmenu():
    menus.index_redirect = '/admin/support'
    manager_menu.append(Menu("support", "Техническая поддержка", "/admin/support/"));
