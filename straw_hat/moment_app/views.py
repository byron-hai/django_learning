# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Category, MomentPost, MomentPostForm


def moment(request):
    docs = MomentPost.objects.all()[:4]
    latest = MomentPost.objects.all()[0]
    category = Category.objects.all()
    return render(request, "moment.html", {'docs': docs,
                                           'category': category,
                                           'latest': latest, })


def keep_moment(request):
    if request.POST.get('keep_moment'):
        form = MomentPostForm(request.POST)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.pub_date = timezone.now()
            doc.save()
            return redirect('moment')
    else:
        form = MomentPostForm
        return render(request, "new.html", {'form': form})

