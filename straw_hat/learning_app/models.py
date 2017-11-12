# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


TYPES = (('Original', 'Original'),
         ('Reprinted', 'Reprinted'),
         ('Translated', 'Translated'),)


class Category(models.Model):
    category_name = models.CharField(max_length=100, null=False, default='New one')

    def __unicode__(self):
        return self.categoryName


class SubCategory(models.Model):
    category_name = models.CharField(max_length=100, null=False, default='New one')
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.category_name


class Images(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, default='Description for this pic')
    img = models.ImageField(upload_to='images/pics', null=True)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title


class DocPost(models.Model):
    title = models.CharField(max_length=100, default='Title')
    doc_type = models.CharField(max_length=20, choices=TYPES, default=1,)
    link = models.URLField(max_length=200, null=True)
    contents = models.TextField()
    img = models.ForeignKey(Images, null=True, blank=True)
    category = models.ForeignKey(SubCategory)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-update_date',)

    def __unicode__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=100, default=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(SubCategory, default=None)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return self.title
