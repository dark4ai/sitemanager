# -*- coding: utf-8 -*-
import menus
from django.conf import settings

def manager_consts(request):
    manager_menu = menus.manager_menu
    current_menu = menus.current_menu
    SITE_ADRESS = settings.SITE_ADRESS
    SITE_NAME = settings.SITE_NAME
    return locals()
