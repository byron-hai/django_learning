# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import BlogPost
from .models import UserInfo


admin.site.register(BlogPost)
admin.site.register(UserInfo)

# Register your models here.
