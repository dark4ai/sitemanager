# -*- coding: utf-8 -*-
from django.template import Library, Node, TemplateSyntaxError
from datetime import date

register = Library()

def good_date(d):
    months = {1:u'января', 2:u'февраля', 3:u'марта', 4:u'апреля', 5:u'мая', 6:u'июня', 7:u'июля', 8:u'августа', 9:u'сентября', 10:u'октября', 11:u'ноября', 12:u'декабря'}
    return u"{0} {1}".format(d.day, months[d.month])

def good_month(m):
    m = int(m)
    months = {1:u'января', 2:u'февраля', 3:u'марта', 4:u'апреля', 5:u'мая', 6:u'июня', 7:u'июля', 8:u'августа', 9:u'сентября', 10:u'октября', 11:u'ноября', 12:u'декабря'}
    return months[m]

register.filter('good_date', good_date)
register.filter('good_month', good_month)
