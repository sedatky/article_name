# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Department
import datetime
# Create your views here.
from django.test import TestCase


def index(request):
    all_article=Department.objects.all()
    html=''
    for article in all_article:
        url='/people/' + str(article.id)+'/'
        html+='<a href="' + url + '">'+ article.deparments_names+ '</a><br>'
    now=datetime.datetime.now()
    return HttpResponse(html)

def article_details(request, article_id):

    return HttpResponse("<h2>Article id: %s<h2>"%str(article_id))
