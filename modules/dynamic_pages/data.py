# -*- coding: utf-8 -*-
from django.conf import settings
from models import Page

print "Insert dynamic_pages in db...";
for page, urlname in settings.DYNAMIC_PAGES:
    Page.objects.get_or_create(name=urlname);
