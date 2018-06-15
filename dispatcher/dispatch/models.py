# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Customer(models.Model):
    usn = models.CharField(max_length=1000)
    cName= models.CharField(max_length=1000)
    address= models.CharField(max_length=2000)
    city = models.CharField(max_length=1000)
    kcity = models.CharField(max_length = 1000,default="")
    ckName=models.CharField(max_length=2000,default="")
    numberofbox=models.CharField(max_length=100,default="")
    def __unicode__(self):
        return self.cName

    def get_absolute_path(self):
        return reverse('primary1',kwargs={'pk':self.pk})