#-*- coding:utf-8 -*-
from sitemanager import menus
from sitemanager.menus import Menu, manager_menu

def setmenu():
    manager_menu.append(Menu("statistics", "Статистика", "/admin/statistics/"));
