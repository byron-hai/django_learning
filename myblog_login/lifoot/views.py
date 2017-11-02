# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import *
from datetime import datetime


def about(request):
    return render(request, "about.html",)


def blog(request):
    posts = BlogPost.objects.all()[:4]
    return render(request, "blog.html", {'posts': posts})


def home(request):
    if request.user.is_authenticated():
        log_tag = 'logout'
    else:
        log_tag = 'login'
         
    return render(request, 'home.html', {'log_tag': log_tag},)


def learn(request):
    return render(request, "learning.html",)


def life_eden(request):
    return render(request, "lifeeden.html",)


def get_posts(requests):
    posts = Post.objects.filter(published=True)
    return render(request, 'lifeeden', {'posts': posts})


def create_blog(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = datetime.now()
            post.update_time = datetime.now()
            post.save()
            return redirect('blog')
    else:
        return render(request, "createblog.html", {'form': BlogPostForm()})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

