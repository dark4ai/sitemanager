# -*- coding: utf-8 -*-
from django.template import Library, Node, TemplateSyntaxError
from datetime import date

register = Library()

months = {1:u'января', 2:u'февраля', 3:u'марта', 4:u'апреля', 5:u'мая', 6:u'июня', 7:u'июля', 8:u'августа', 9:u'сентября', 10:u'октября', 11:u'ноября', 12:u'декабря'}

def good_date(d):
    return u"{0} {1}".format(d.day, months[d.month])

def good_fdate(d):
    return u"{0} {1} {2}".format(d.day, months[d.month], d.year)

def good_month(m):
    m = int(m)
    return months[m]

def good_datetime(d):
    return u"{0} {1}".format(good_fdate(d), d.strftime("%H:%M:%S"))

def good_fdatetime(d):
    return u"{0} {1}".format(good_fdate(d), d.strftime("%H:%M"))

register.filter('good_datetime', good_datetime)
register.filter('good_fdatetime', good_fdatetime)
register.filter('good_date', good_date)
register.filter('good_fdate', good_fdate)
register.filter('good_month', good_month)
