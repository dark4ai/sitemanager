# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

def upload_path(instance, filename):
    return u"images/models/datapages/%d.jpg" % instance.pk

class DataPage(models.Model):
    title = models.TextField()
    preview = models.TextField(blank=True)
    content = models.TextField()
    date = models.DateField(default=datetime.now)
    pageset = models.CharField(max_length=32)
    is_public = models.BooleanField(default=True)
    image = ThumbnailerImageField(
            blank=True,
            upload_to=upload_path,
            resize_source=dict(size=(640, 640))
    )

    def __unicode__(self):
        return self.title

    def get_prev(self):
        prev = DataPage.objects.filter(date__lt=self.date, is_public=True, pageset=self.pageset).order_by('-date')
        if prev:
            return prev[0]
        return False

    def get_next(self):
        next = DataPage.objects.filter(date__gt=self.date, is_public=True, pageset=self.pageset).order_by('date')
        if next:
            return next[0]
        return False

