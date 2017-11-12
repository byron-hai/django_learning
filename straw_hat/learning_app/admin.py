# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Images)
admin.site.register(DocPost)
admin.site.register(Video)
