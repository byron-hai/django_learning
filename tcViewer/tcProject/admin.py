from __future__ import unicode_literals
from django.contrib import admin
from .models import *
# Register your models here.


class GeneralTcNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'sw_revision', 'fw_version', 'app_version', 'tc_result', 'tc_status', 'owner')


class RelTcSumAdmin(admin.ModelAdmin):
    list_display = ('sw_revision', 'create_date', 'schedule_start', 'schedule_end', 'finish_date', 'status', 'progress')


admin.site.register(ProjectCategory)
admin.site.register(TcProject)
admin.site.register(TcStatus)
admin.site.register(SupportedKernels)
admin.site.register(SupportedOSType)
admin.site.register(GeneralTcNote, GeneralTcNoteAdmin)
admin.site.register(ReleaseTcSummary, RelTcSumAdmin)
