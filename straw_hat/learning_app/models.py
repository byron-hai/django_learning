# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE


TYPES = (('Original', 'Original'),
         ('Reprinted', 'Reprinted'),
         ('Translated', 'Translated'),)


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default='Add+')

    def __unicode__(self):
        return self.name


class SubCategory(models.Model):
    category_name = models.CharField(max_length=100, blank=True, default='Add+')
    parent = models.ForeignKey(Category)

    def __unicode__(self):
        return self.category_name


class Images(models.Model):
    title = models.CharField(max_length=100, default='None')
    description = models.CharField(max_length=255, blank=True, default='Description for this pic')
    img = models.ImageField(upload_to='images/pics', default='image')

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title


class DocPost(models.Model):
    title = models.CharField(max_length=100, default='Title')
    doc_type = models.CharField(max_length=20, choices=TYPES, default=1,)
    category = models.ForeignKey(SubCategory)
    contents = HTMLField('Content')
    view_num = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=False)

    class Meta:
        ordering = ('-update_date',)

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
        exclude = ('pub_date', 'update_date', 'view_num')


class Video(models.Model):
    title = models.CharField(max_length=100, default=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(SubCategory, default=None)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return self.title

