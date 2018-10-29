from django.contrib import admin
from .models import *


class FWReleaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'version', 'fw_type', 'rel_date')


class SWReleaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'revision', 'branch', 'rel_date')


class AppReleaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'version', 'branch', 'rel_date')


admin.site.register(FirmwareType)
admin.site.register(SoftwareBranch)
admin.site.register(AppType)
admin.site.register(FirmwareRelease, FWReleaseAdmin)
admin.site.register(SoftwareRelease, SWReleaseAdmin)
admin.site.register(AppRelease, AppReleaseAdmin)
