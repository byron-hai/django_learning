# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Category, SubCategory, DocPost, DocPostForm
from datetime import datetime


def learning(request):
    category = Category.objects.all()
    sub_category = SubCategory.objects.all()
    docs = DocPost.objects.all()[:4]
    return render(request, "learning.html", {'docs': docs,
                                             'category': category,
                                             'sub_category': sub_category})


def new_document(request):
    if request.POST.get("new_doc"):
        form = DocPostForm(request.POST)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.pub_date = datetime.now()
            doc.update_date = datetime.now()
            doc.save()
            return redirect('learning')
    else:
        form = DocPostForm
        return render(request, "newdoc.html", {'form': form})
