# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def index(request):

    text = "HelloWorld"
    return render(request, 'index.html', {'text': text})


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, "about.html", )



