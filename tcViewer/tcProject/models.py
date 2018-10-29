from django.db import models
from django.contrib.auth.models import User
from sfxRelease.models import FirmwareRelease, SoftwareRelease, AppRelease
from sfxProduct.models import Product
from django.utils.text import slugify


class TcProject(models.Model):
    name = models.CharField(max_length=200, default='Project name',
                            help_text="The name of test item. Max length is 200")
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200, blank=True)
    tc_feature = models.TextField(verbose_name='test features', blank=True,
                                  help_text="If more features, separate them by ';'")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TcProject, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Test Projects"
        ordering = ['name']


class SupportedKernels(models.Model):
    OS_TYPE = (
        ('ubuntu', 'Ubuntu'),
        ('centos', 'CentOS'),
        ('debian', 'Debian'),
    )

    kernel = models.CharField(max_length=30, unique=True)
    os_type = models.CharField(max_length=10, choices=OS_TYPE, default='ubuntu')

    def __str__(self):
        return "{} {}".format(self.kernel, self.os_type)

    class Meta:
        verbose_name_plural = "Supported Kernels"


class TcStatus(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class GeneralTcNote(models.Model):
    TC_RESULT = (
        ('PASS', 'PASS'),
        ('FAIL', 'FAIL'),
        ('N/A', 'N/A'),
        ('-', '-'),
    )

    name = models.ForeignKey(TcProject, on_delete=models.CASCADE)
    device = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default='')
    sw_revision = models.ForeignKey(SoftwareRelease, on_delete=models.SET_DEFAULT, default='')
    fw_version = models.ForeignKey(FirmwareRelease, on_delete=models.SET_DEFAULT, default='')
    app_version = models.ForeignKey(AppRelease, on_delete=models.SET_DEFAULT, default='')
    tc_kernels = models.TextField()
    tc_link = models.URLField(blank=True)
    tc_loop = models.SmallIntegerField(default=1)
    tc_result = models.CharField(max_length=8, choices=TC_RESULT, default='-')
    tc_status = models.ForeignKey(TcStatus, on_delete=models.CASCADE)
    tc_progress = models.SmallIntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='')
    create_date = models.DateField(auto_now_add=True)
    schedule_start = models.DateField()
    schedule_end = models.DateField()
    note = models.TextField(blank=True)

    def __str__(self):
        return "{prj_name} {sw} {fw} {result} {status} {owner}".format(prj_name=self.name,
                                                                       sw=self.sw_revision,
                                                                       fw=self.fw_version,
                                                                       result=self.tc_result,
                                                                       status=self.tc_status,
                                                                       owner=self.owner)

    class Meta:
        verbose_name_plural = "Test Notes"
        ordering = ['name', 'sw_revision', '-schedule_start']


class ReleaseTcSummary(models.Model):
    sw_revision = models.ForeignKey(SoftwareRelease, on_delete=models.SET_DEFAULT, default='')
    tc_projects = models.ManyToManyField(TcProject)
    create_date = models.DateField(auto_now_add=True)
    schedule_start = models.DateField()
    schedule_end = models.DateField()
    status = models.ForeignKey(TcStatus, on_delete=models.CASCADE)
    progress = models.SmallIntegerField(default=0)

    def __str__(self):
        return "{sw} {status} {progress}".format(sw=self.sw_revision, status=self.status, progress=self.progress)

    class Meta:
        ordering = ['-sw_revision']
