# -*- coding: utf-8 -*-
from django import http, template
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from sitemanager.context_processors import manager_consts
from sitemanager.menus import current_menu
from sitemanager import menus
from models import Page

def view_page(request, page, urlname):
    menus.current_menu = "dp_" + urlname
    context_instance = template.RequestContext(request, processors=[manager_consts])
    p = Page.objects.get(name=urlname)
    return render_to_response('cms/modules/dynamic_pages/index.html', {"urlname":urlname, "page":page, "content":p.content}, context_instance=context_instance)

def save_page(request):
    if request.method == 'POST' and 'urlname' in request.POST and 'content' in request.POST:
        try:
            p = Page.objects.get(name=request.POST['urlname'])
            p.content = request.POST['content']
            p.save()
            return HttpResponseRedirect('/admin/dynamic_pages/%s' % p.name)
        except ObjectDoesNotExist:
            return Http404()
    else:
        return Http404()
