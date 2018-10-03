# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class process(models.Model):
    id  = models.AutoField(primary_key=True)
    process = models.CharField(max_length = 100)

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    DateofReport = models.DateField()
    Process = models.CharField(max_length = 100)
    Hours = models.IntegerField()
    
class datesofmonth(models.Model):
    id = models.AutoField(primary_key=True)
    weekday = models.DateField()    