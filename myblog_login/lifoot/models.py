# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media')

    class Meta:
        ordering = ('-created')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])


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

