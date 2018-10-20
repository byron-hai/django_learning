# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class FwType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "FW_types"


class FwRelease(models.Model):
    version = models.CharField(max_length=20, defualt='')
    fw_type = models.ForeignKey(FwType, on_delete=models.CASECADE)
    rel_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "{}_{}".format(self.fw_type, self.version)

    class Meta:
        verbose_name_plural = "FW_Releases"


class DrvBranch(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Drver branches"


class DriverRelease(models.Model):
    revision = models.CharField(max_length=20, defualt='')
    branch = models.ForeignKey(User, on_delete=models.CASECADE)
    rel_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "{} {}".format(self.branch, self.revision)


class AppRelease(models.Model):
    version = models.CharField(max_length=20, default='')
    rel_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.version

class ProductType(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product types"

class Product(models.Model):
    name = models.CharField(max_length=20, default='')
    pro_type = models.ForeignKey(ProductType, on_delete=models.CASECADE)

    
class Contributor(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.username

    class Meta:
        ordering = ('name',)


class Advise(models.Model):
    message = models.TextField()
    send_date = models.DateField(default=timezone.now)

    def __str__(self):
        return '%s, Topic: %s' % (str(self.send_date), self.message[:100])

    class Meta:
        ordering = ('-send_date',)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=None)
    image = models.ImageField(upload_to='profile_image/', default='profile_image/img-default.jpg')
    description = models.CharField(max_length=255, default='')
    signature = models.CharField(max_length=200, default='')
    wechat = models.ImageField(upload_to='wechat_image/', default='wechat_image/wechat.jpg')
    github = models.URLField(default='')

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "user-profiles"

    def __str__(self):
        return self.user.username

