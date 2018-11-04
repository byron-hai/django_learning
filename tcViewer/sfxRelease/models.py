# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class FirmwareType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100, blank=True, help_text="Simply description in less than 100 letters")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Firmware Types"


class FirmwareRelease(models.Model):
    version = models.CharField(max_length=20, unique=True)
    fw_type = models.ForeignKey(FirmwareType, on_delete=models.DO_NOTHING)
    rel_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{}_{}".format(self.fw_type, self.version)

    class Meta:
        verbose_name_plural = "Firmware Releases"
        ordering = ['fw_type', '-version', 'rel_date']


class SoftwareBranch(models.Model):
    branch = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100, blank=True, default="Simply description in less than 100 letters")

    def __str__(self):
        return self.branch

    class Meta:
        verbose_name_plural = "Software Branches"


class SoftwareRelease(models.Model):
    revision = models.CharField(max_length=20, unique=True)
    branch = models.ForeignKey(SoftwareBranch, on_delete=models.DO_NOTHING)
    rel_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{}_{}".format(self.branch, self.revision)

    class Meta:
        verbose_name_plural = "Software Releases"
        ordering = ['branch', '-revision', '-rel_date']


class AppType(models.Model):
    branch = models.CharField(max_length=30, unique=True, help_text='Application branches')
    description = models.CharField(max_length=100, blank=True, default="Simply description in less than 100 letters")

    def __str__(self):
        return self.branch

    class Meta:
        verbose_name_plural = "Application Types"


class AppRelease(models.Model):
    version = models.CharField(max_length=20, unique=True)
    branch = models.ForeignKey(AppType, on_delete=models.DO_NOTHING)
    rel_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.version

    class Meta:
        verbose_name_plural = "Application Releases"
        ordering = ['-version', '-rel_date']
