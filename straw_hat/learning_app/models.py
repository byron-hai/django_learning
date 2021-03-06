# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
#from django.conf import settings
from django import forms
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE


TYPES = (('Original', 'Original'),
         ('Reprinted', 'Reprinted'),
         ('Translated', 'Translated'),)


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='sons')

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.name


class SubCategory(models.Model):
    category_name = models.CharField(max_length=100, null=False, blank=False)
    parent = models.ForeignKey(Category, blank=True, null=True, related_name='children')

    class Meta:
        verbose_name_plural = "sub-categories"

    def __unicode__(self):
        return self.category_name


class DocPost(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=100)
    doc_type = models.CharField(max_length=20, choices=TYPES, default=1,)
    category = models.ForeignKey(SubCategory, null=True, blank=True)
    contents = HTMLField('Content')
    view_num = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False,)
    draft = models.BooleanField(default=False)

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class DocPostForm(forms.ModelForm):
    contents = forms.CharField(
        widget=TinyMCEWidget(attrs={'required': False,
                                    'cols': 30,
                                    'rows': 10}))

    class Meta:
        model = DocPost
        fields = '__all__'
        exclude = ('pub_date', 'view_num')

