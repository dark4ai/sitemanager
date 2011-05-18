# -*- coding: utf-8 -*-
from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=50, unique=True)
    content = models.TextField()

    def __unicode__(self):
        return self.name
