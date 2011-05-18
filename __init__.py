from sitemanager.sites import SiteManager, site
from sitemanager.menus import manager_menu
from django.conf import settings
from django.utils.importlib import import_module

def init():
    for module in settings.SITEMANAGER_MODULES:
        m = import_module(module)
        try:
            setmenu = getattr(m, 'setmenu')
            setmenu()
        except AttributeError:
            pass
        site.modules.append(m)
