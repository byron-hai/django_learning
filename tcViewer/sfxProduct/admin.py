from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial_number', 'opn', 'model', 'capacity')


admin.site.register(Model)
admin.site.register(OPN)
admin.site.register(SN)
admin.site.register(Capacity)
admin.site.register(Product, ProductAdmin)
