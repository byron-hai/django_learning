# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django import forms


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=60)
    body = models.TextField()
    pub_date = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        ordering = ("-pub_date",)

    def __unicode__(self):
        return self.title


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('pub_date', 'update_time', )


class UserInfo(models.Model):
    user_type_list = ((1, 'user'), (2, 'admin'), )
    user_type = models.IntegerField(choices=user_type_list, default=1)

    name = models.CharField(max_length=30)
    email = models.EmailField()
    memo = models.TextField()

    def __unicode__(self):
        return self.name

