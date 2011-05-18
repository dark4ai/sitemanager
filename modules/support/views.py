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
from forms import CallForm
from django.conf import settings

@menu_decorator("support")
def support(request, form_status=False):
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = u'Предложение с сайта %s' % (settings.SITE_NAME)
            message = u'''Адрес %s\r\n\r\nИмя: %s\r\nСообщение: %s''' % (settings.SITE_ADRESS, cd['name'], cd['message'])
            send_mail(subject, message, settings.SITE_EMAIL, [settings.ADMINS[0][1]])
            return HttpResponseRedirect('/admin/support/success/')
    else:
        form = CallForm()
    return sm_template(request,'cms/modules/support/index.html', locals())
