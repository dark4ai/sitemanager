#-*- coding:utf-8 -*-
from django import forms
import re

class CallForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
