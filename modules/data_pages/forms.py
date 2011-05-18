from django import forms
from django.forms import ModelForm
from models import DataPage

class DataPageForm(ModelForm):
    class Meta:
        model = DataPage
#       exclude = ('pageset',)
    #   fields = ('title', 'content', 'date', 'image')
        widgets = {
            'pageset':forms.HiddenInput(),
            'title':forms.Textarea(attrs={"rows":4}),
            'content':forms.Textarea(attrs={"id":"editor_content", "class":"w100", "style":"height: 500px;"}),
            'preview':forms.Textarea(attrs={"rows":6}),
        }
