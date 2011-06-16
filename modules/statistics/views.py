#-*- coding:utf-8 -*-
from django import http, template
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.core.mail import send_mail
from sitemanager.context_processors import manager_consts
from sitemanager.menus import current_menu
from sitemanager.decorators import menu_decorator
from sitemanager.shortcuts import sm_template
from django.conf import settings
from django.utils import simplejson
from urllib2 import urlopen, URLError
from urllib import urlencode
from datetime import timedelta, date

@menu_decorator('statistics')
def statistics(request):
    return sm_template(request,'cms/modules/statistics/index.html', locals())
URLError
def ya_api(request, range='week'):
    date2 = date.today()
    date1 = date2 - timedelta(days=6)
    group = 'day'
    if range == 'month':
        date1 = date2 - timedelta(days=29)
    if range == 'year':
        date1 = date2 - timedelta(days=364)
        group = 'month'
    params = {
            'id': settings.STATISTICS_COUNTER_ID,
            'oauth_token': settings.STATISTICS_OAUTH_TOKEN,
            'date1': date1.strftime('%Y%m%d'),
            'date2': date2.strftime('%Y%m%d'),
    }
    try:
        json = urlopen("http://api-metrika.yandex.ru/stat/traffic/summary.json?%s" % urlencode(params))
    except URLError:
        json = {"errors": [{
                            "text": u"К сожалению metrika.yandex.ru не отвечает",
                            "code": u"ERR_TIMEOUT"
                            }]};
        result = simplejson.dumps(json, ensure_ascii=False)
        return HttpResponse(result, mimetype='application/json')
    return HttpResponse(json.read(), mimetype='application/json')
