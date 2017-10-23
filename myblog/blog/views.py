# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from datetime import datetime
from blog.models import *
from .forms import SignupForm


def archive(request):
    posts = BlogPost.objects.all()[:4]
    return render(request, "archive.html", {'posts': posts, 'form': BlogPostForm()})


def create_blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = datetime.now()
            post.update_time = datetime.now()
            post.save()

            return HttpResponseRedirect('/blog/')
    else:
        posts = BlogPost.objects.all()[:3]
        return render(request, "archive.html", {'posts': posts, 'form': BlogPostForm()})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = NameForm()
    return render(request, 'home.html', {'form': form})
