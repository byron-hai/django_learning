from django.db import models
from django.contrib.auth.models import User
from sfxRelease.models import FirmwareRelease, SoftwareRelease, AppRelease
from sfxProduct.models import Product


class ProjectCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Project Categories'


class TcProject(models.Model):
    name = models.CharField(max_length=200, default='Project name',
                            help_text="The name of test item. Max length is 200")
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=200, blank=True)
    tc_feature = models.TextField(verbose_name='test features', blank=True,
                                  help_text="If more features, separate them by ';'")

    def __str__(self):
        return "{} - {}".format(self.category, self.name)

    class Meta:
        verbose_name_plural = "Test Projects"
        ordering = ['category', 'name']


class SupportedOSType(models.Model):
    os_name = models.CharField(max_length=10, default='ubuntu', help_text='OS name like Ubuntu, CentOS')
    
    def __str__(self):
        return self.os_name
    
    
class SupportedKernels(models.Model):
    kernel = models.CharField(max_length=30, unique=True)
    os_type = models.ForeignKey(SupportedOSType, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{} {}".format(self.kernel, self.os_type)

    class Meta:
        verbose_name_plural = "Supported Kernels"


class TcStatus(models.Model):
    name = models.CharField(max_length=20, default='Not-Started')

    def __str__(self):
        return self.name


class GeneralTcNote(models.Model):
    TC_RESULT = (
        ('PASS', 'PASS'),
        ('FAIL', 'FAIL'),
        ('N/A', 'N/A'),
        ('-', '-'),
    )

    project = models.ForeignKey(TcProject, on_delete=models.DO_NOTHING)
    device = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True)
    sw_revision = models.ForeignKey(SoftwareRelease, on_delete=models.DO_NOTHING, blank=True, null=True)
    fw_version = models.ForeignKey(FirmwareRelease, on_delete=models.DO_NOTHING, blank=True, null=True)
    app_version = models.ForeignKey(AppRelease, on_delete=models.DO_NOTHING, blank=True, null=True)
    tc_os = models.TextField(help_text='OS environment', blank=True, null=True)
    tc_link = models.URLField(blank=True, null=True)
    tc_loop = models.SmallIntegerField(default=1)
    tc_result = models.CharField(max_length=8, choices=TC_RESULT, default='-')
    tc_status = models.ForeignKey(TcStatus, on_delete=models.DO_NOTHING)
    tc_progress = models.SmallIntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_date = models.DateField(auto_now_add=True)
    schedule_start = models.DateField(blank=True, null=True)
    schedule_end = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{prj_name} {sw} {fw} {result} {status} {owner}".format(prj_name=self.project,
                                                                       sw=self.sw_revision,
                                                                       fw=self.fw_version,
                                                                       result=self.tc_result,
                                                                       status=self.tc_status,
                                                                       owner=self.owner)

    class Meta:
        verbose_name_plural = "Test Notes"
        ordering = ['-schedule_end', 'sw_revision', 'project']


class ReleaseTcSummary(models.Model):
    sw_revision = models.ForeignKey(SoftwareRelease, on_delete=models.DO_NOTHING)
    tc_projects = models.ManyToManyField(TcProject, blank=True)
    create_date = models.DateField(auto_now_add=True)
    schedule_start = models.DateField(blank=True, null=True)
    schedule_end = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    status = models.ForeignKey(TcStatus, on_delete=models.DO_NOTHING)
    progress = models.SmallIntegerField(default=0)  # Definition based on Group test processes,

    def __str__(self):
        return "{sw} {status} {progress}".format(sw=self.sw_revision, status=self.status, progress=self.progress)

    class Meta:
        verbose_name_plural = 'Release Test Summaries'
        ordering = ['-schedule_end', 'sw_revision']


'''
class GroupTcSummary(models.Model):
    name = models.ForeignKey(ProjectCategory, on_delete=models.DO_NOTHING)
    sw_revision = models.ForeignKey(SoftwareRelease, on_delete=models.DO_NOTHING)
    tc_projects = models.ManyToManyField(TcProject)
    create_date = models.DateField(auto_now_add=True)
    schedule_start = models.DateField(blank=True, null=True)
    schedule_end = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    status = models.ForeignKey(TcStatus, on_delete=models.DO_NOTHING)
    progress = models.SmallIntegerField(default=0)   # Definition based on tc_projects' progresses


class TcComments(models.Model):
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_date = models.DateField(auto_now_add=True)
    note_id = models.IntegerField()

    def __str__(self):
        return "{} {} {}".format(self.note_id, self.owner, self.create_date, self.content)

    class Meta:
        verbose_name_plural = "test coments"
        ordering = ('-create_date', '-note_id', 'owner')
'''
