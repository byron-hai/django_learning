# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.name


class MomentPost(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, blank=True)
    contents = HTMLField('Content')
    view_num = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False,)
    draft = models.BooleanField(default=False)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = "moment-posts"

    def __unicode__(self):
        return self.title


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class MomentPostForm(forms.ModelForm):
    contents = forms.CharField(
        widget=TinyMCEWidget(attrs={'required': False,
                                    'cols': 30,
                                    'rows': 10}))

    class Meta:
        model = MomentPost
        fields = '__all__'
        exclude = ('pub_date', 'view_num')

