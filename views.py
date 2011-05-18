from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from sitemanager.menus import menu_decorator

def test(request):
    return HttpResponse("Hello, world");
