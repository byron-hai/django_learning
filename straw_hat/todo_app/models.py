# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django import forms


STATES = (('Not-Started', 'Not-Started'),
          ('Ongoing', 'Ongoing'),
          ('Delayed', 'Delayed'),
          ('Finished', 'Finished'),
          ('Canceled', 'Canceled'),)

IMPORT_WEIGHT = (('High', 'High'),
                 ('Middle', 'Middle'),
                 ('Low', 'Low'),
                 ('General', 'General'),)


class TodoThisYear(models.Model):
    task = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATES, default='Not-Started')
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    importance = models.CharField(max_length=10, choices=IMPORT_WEIGHT, default='General')
    finished = models.DecimalField(max_digits=3, default="0", decimal_places=0, help_text="Percentage, from 0 to 100")

    class Meta:
        ordering = ('start_date',)

    def __unicode__(self):
        return '%s, %s' % (self.task, self.status)


class TodoThisYearForm(forms.ModelForm):
    class Meta:
        model = TodoThisYear
        widgets = {
            'task': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
        }
        exclude = ('status', 'create_date', 'finished')


class TodoThisDay(models.Model):
    task = models.TextField()
    time = models.TimeField(help_text="Time format e.g. : 12:20")
    status = models.CharField(max_length=20, choices=STATES, default='Not-Started')
    importance = models.CharField(max_length=10, choices=IMPORT_WEIGHT, default='General')
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    
    class Meta:
        ordering = ('time',)

    def __unicode__(self):
        return '%s, %s, %s' % (self.time, self.task, self.status)


class TodoThisDayForm(forms.ModelForm):
    class Meta:
        model = TodoThisDay
        widgets = {
            'task': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
        }
        exclude = ('status', 'create_date',)
