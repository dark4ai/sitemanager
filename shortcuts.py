# -*- coding: utf-8 -*-
from django import http, template
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from sitemanager.context_processors import manager_consts

def sm_template(request, t, extra_context=None):
	if extra_context is None:
		extra_context = {}
	context_instance = template.RequestContext(request, processors=[manager_consts])
	return render_to_response(t, extra_context, context_instance=context_instance)
