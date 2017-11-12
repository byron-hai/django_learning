# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime
from .models import TodoThisYear, TodoThisYearForm, TodoThisMonth, TodoThisMonthForm, TodoThisDay, TodoThisDayForm


STATES = ('Not-Started',
          'Ongoing',
          'Delayed',
          'Delayed',
          'Finished',
          'Canceled',)


IMPORT_WEIGHT = ('High',
                 'Middle',
                 'Low',
                 'General',)


def todo_today(request):
    if request.POST.get("plan_today"):
        form = TodoThisDayForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_date = datetime.now().date()
            task.create_date = datetime.now()
            task.save()
            return redirect('todo_today')
    else:
        plan_d_form = TodoThisDayForm()
        tasks_today = TodoThisDay.objects.all()
        task_ids = TodoThisDay.objects.order_by().values_list('id', flat=True).distinct()
        return render(request, "todo_today.html", {'day_form': plan_d_form,
                                                   'tasks_today': tasks_today,
                                                   'task_ids': task_ids, })


def todo_monthly(request):
    if request.POST.get("plan_this_month"):
        form = TodoThisMonthForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.create_date = datetime.now()
            task.finished = 0
            task.save()
            return redirect('todo_monthly')
    else:
        plan_m_form = TodoThisMonthForm()
        tasks_this_month = TodoThisMonth.objects.all()
        task_ids = TodoThisMonth.objects.order_by().values_list('id', flat=True).distinct()
        return render(request, "todo_monthly.html", {'month_form': plan_m_form,
                                                     'tasks_this_month': tasks_this_month,
                                                     'task_ids': task_ids, })


def todo_yearly(request):
    if request.POST.get("plan_long_term"):
        form = TodoThisDayForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.status = 'Not-Started'
            task.create_date = datetime.now()
            task.save()
            return redirect('todo_yearly')
    else:
        plan_y_form = TodoThisYearForm()
        tasks_year = TodoThisYear.objects.all()
        task_ids = TodoThisYear.objects.order_by().values_list('id', flat=True).distinct()
        return render(request, "todo_yearly.html", {'year_form': plan_y_form,
                                                    'tasks_year': tasks_year,
                                                    'task_ids': task_ids, })
