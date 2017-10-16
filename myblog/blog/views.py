# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from blog.models import *


def archive(request):
    posts = BlogPost.objects.all()[:3]
    return render(request, "archive.html", {'posts': posts, 'form': BlogPostForm()}, RequestContext(request))


def create_blogpost(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = datetime.now()
            post.update_time = datetime.now()
            post.save()

    return HttpResponseRedirect('/blog/')


