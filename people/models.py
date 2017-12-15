# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Department(models.Model):
    deparments_names=models.CharField(max_length=250)
    faculty = models.CharField(max_length=250)
    academician_name=models.CharField(max_length=50)



class Article(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    article_name=models.CharField(max_length=500)

