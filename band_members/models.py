# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Band_Member(models.Model):
    """
        MODEL CONTAINS NIGHTBLIND BAND DETAILS
        -   short_name
        -   name
        -   instrument
        -   gear
    """
    short_name = models.CharField(max_length=100,null=False)
    name = models.CharField(max_length=100,null=False)
    instrument = models.CharField(max_length=150,null=False)
    gear = models.CharField(max_length=150,null=False)
    img = models.CharField(max_length=150,null=False)

    def __unicode__(self):
        return self.name
