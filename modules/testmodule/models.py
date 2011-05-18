# -*- coding: utf-8 -*-
from django.db import models


class Person(models.Model):
    nick = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    def __unicode__(self):
        return self.nick
