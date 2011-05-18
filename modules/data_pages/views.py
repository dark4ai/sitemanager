# -*- coding: utf-8 -*-
from datetime import datetime
from django import http, template
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.utils.html import strip_tags
from django.template.defaultfilters import truncatewords
from django.conf import settings
from sitemanager.context_processors import manager_consts
from sitemanager.menus import current_menu
from sitemanager.shortcuts import sm_template
from sitemanager import menus
from sitemanager.decorators import menu_decorator
from sitemanager.templatetags.numerals import num_func
from sitemanager import menus
from models import DataPage
from forms import DataPageForm
import urls

def pages(request, pageset):
    if not pageset in urls.list_pages:
        raise Http404
    forms = urls.morfology_pages[pageset][0]
    nforms = urls.morfology_pages[pageset][1]
    menus.current_menu = "datapage_" + pageset
    pages = DataPage.objects.filter(pageset = pageset).order_by('-pk')
    return sm_template(request, 'cms/modules/data_pages/pages.html', {"pages":pages, "pages_forms":forms, "pages_nforms":nforms, "pages_len":len(pages)})

def page(request, pageset, page_id=None):
    if not pageset in urls.list_pages:
        raise Http404()
    forms = urls.morfology_pages[pageset][0]
    nforms = urls.morfology_pages[pageset][1]
    title = None
    img = None
    menus.current_menu = "datapage_" + pageset
    if request.method == 'POST':
        if page_id == None:
            f = DataPageForm(request.POST, request.FILES)
        else:
            try:
                page_id = int(page_id)
                page = DataPage.objects.get(pk=page_id)
                img = page.image
                f = DataPageForm(request.POST, request.FILES, instance=page)
            except (DataPage.DoesNotExist, ValueError):
                raise Http404()
        if f.is_valid():
            datapage = f.save(commit=False)
            s = settings
            if not datapage.preview:
                datapage.preview = truncatewords(strip_tags(datapage.content), settings.DATA_PAGES_PREVIEW_WORDS)
            datapage.save()
            return HttpResponseRedirect("/admin/data_pages/%s/pages/" % pageset)
        return sm_template(request, 'cms/modules/data_pages/page.html', {"pform":f, "pages_nforms":nforms, "pages_forms":forms, "img":img})
    if page_id == None:
#           p = DatePage()
#           p.pageset = pageset
            f = DataPageForm(initial={"pageset":pageset})
    else:
        try:
            page_id = int(page_id)
            page = DataPage.objects.get(pk=page_id)
            img = page.image
            f = DataPageForm(instance=page)
            title = page.title
        except (DataPage.DoesNotExist, ValueError):
            raise Http404()
    return sm_template(request, 'cms/modules/data_pages/page.html', {"pform":f, "pages_nforms":nforms, "pages_forms":forms, "title":title, "img":img})

def delete_page(request, page_id):
    try:
        page_id = int(page_id)
        page = DataPage.objects.get(pk=page_id)
        pageset = page.pageset
        page.delete()
        pages = DataPage.objects.filter(pageset = pageset)
#       page.delete()
        return HttpResponse("%d %s" % (len(pages), num_func(len(pages), urls.morfology_pages[pageset][1])))
    except (DataPage.DoesNotExist, ValueError):
        raise HttpResponse("bad")
