from django import http, template
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from sitemanager.context_processors import manager_consts
from sitemanager.menus import current_menu
from sitemanager.decorators import menu_decorator

@menu_decorator("testlink")
def test(request):
    context_instance = template.RequestContext(request, processors=[manager_consts])
    return render_to_response('cms/modules/testmodule/index.html', {}, context_instance=context_instance)
