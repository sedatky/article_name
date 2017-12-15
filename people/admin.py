# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
#from __future__ import unicode_literals

from .models import Department
from .models import Article
from django.contrib import admin

# Register your models here.
admin.site.register(Department)
admin.site.register(Article)