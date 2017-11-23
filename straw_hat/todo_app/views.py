# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.utils import timezone
from .models import TodoThisYear, TodoThisYearForm, TodoThisMonth, TodoThisMonthForm, TodoThisDay, TodoThisDayForm


def get_important_weight():
    important_val = ('High',
                     'Middle',
                     'Low',
                     'General',)
    return important_val


def get_execute_status():
    states = ('Not-Started',
              'Ongoing',
              'Delayed',
              'Delayed',
              'Finished',
              'Canceled',)
    return states


def get_finished_val_num():
    return range(0, 101, 10)


def todo_today(request):
    if request.POST.get("plan_today"):
        form = TodoThisDayForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_date = timezone.now().date()
            task.create_date = timezone.now()
            task.save()
            return redirect('todo_today')

    elif request.POST.get("day_plan_update") and request.POST.get('taskId'):
        task_id = request.POST.get('taskId', False)
        if task_id:
            appt_time = request.POST.get('appt_time', False)
            import_val = request.POST.get('importance', False)
            status_val = request.POST.get('status', False)
            if appt_time:
                TodoThisDay.objects.filter(id=task_id).update(task_time=appt_time)
            if import_val:
                TodoThisDay.objects.filter(id=task_id).update(importance=import_val)
            if status_val:
                TodoThisDay.objects.filter(id=task_id).update(status=status_val)

            return redirect('todo_today')
    else:
        cur_date = timezone.now().date()
        plan_d_form = TodoThisDayForm()
        tasks_today = TodoThisDay.objects.filter(task_date=timezone.now(), )
        task_ids = TodoThisDay.objects.filter(task_date=timezone.now()).\
            order_by().values_list('id', flat=True).distinct()
        exe_status = get_execute_status()
        import_all = get_important_weight()
        return render(request, "todo_today.html", {'day_form': plan_d_form,
                                                   'tasks_today': tasks_today,
                                                   'task_ids': task_ids,
                                                   'current_date': cur_date,
                                                   'status_all': exe_status,
                                                   'importance_all': import_all, })


def todo_monthly(request):
    if request.POST.get("plan_this_month"):
        form = TodoThisMonthForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.create_date = timezone.now()
            task.finished = 0
            task.save()
            return redirect('todo_monthly')

    elif request.POST.get("month_plan_update") and request.POST.get('taskId'):
        task_id = request.POST.get('taskId', False)
        if task_id:
            from_date = request.POST.get('fromDate', False)
            to_date = request.POST.get('toDate', False)
            import_val = request.POST.get('importance', False)
            status_val = request.POST.get('status', False)
            finish_val = request.POST.get('finished', False)
            if from_date:
                TodoThisMonth.objects.filter(id=task_id).update(start_date=from_date)
            if to_date:
                TodoThisMonth.objects.filter(id=task_id).update(end_date=to_date)
            if import_val:
                TodoThisMonth.objects.filter(id=task_id).update(importance=import_val)
            if status_val:
                TodoThisMonth.objects.filter(id=task_id).update(status=status_val)
            if finish_val:
                TodoThisMonth.objects.filter(id=task_id).update(finished=finish_val)
            return redirect('todo_monthly')
    else:
        cur_year = timezone.now().year
        cur_month = timezone.now().month
        plan_m_form = TodoThisMonthForm()
        finish_val = get_finished_val_num()
        tasks_this_month = TodoThisMonth.objects.filter(start_date__year__gte=cur_year,
                                                        start_date__month__gte=cur_month,
                                                        end_date__year__lte=cur_year,
                                                        end_date__month__lte=(cur_month+1),)

        task_ids = TodoThisMonth.objects.filter(start_date__year__gte=cur_year,
                                                start_date__month__gte=cur_month,
                                                end_date__year__lte=cur_year,
                                                end_date__month__lte=(cur_month+1),).\
            order_by().values_list('id', flat=True).distinct()
        exe_status = get_execute_status()
        import_all = get_important_weight()
        return render(request, "todo_monthly.html", {'month_form': plan_m_form,
                                                     'tasks_this_month': tasks_this_month,
                                                     'task_ids': task_ids,
                                                     'current_month': cur_month,
                                                     'status_all': exe_status,
                                                     'importance_all': import_all,
                                                     'finish_vals': finish_val, })


def todo_yearly(request):
    if request.POST.get("plan_long_term"):
        form = TodoThisYearForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.create_date = timezone.now()
            task.finished = 0
            task.save()
            return redirect('todo_yearly')

    elif request.POST.get("year_plan_update") and request.POST.get('taskId'):
        task_id = request.POST.get('taskId', False)
        if task_id:
            from_date = request.POST.get('from_date', False)
            to_date = request.POST.get('to_date', False)
            import_val = request.POST.get('importance', False)
            status_val = request.POST.get('status', False)
            finish_val = request.POST.get('finished', False)
            if from_date:
                TodoThisYear.objects.filter(id=task_id).update(start_date=from_date)
            if to_date:
                TodoThisYear.objects.filter(id=task_id).update(end_date=to_date)
            if import_val:
                TodoThisYear.objects.filter(id=task_id).update(importance=import_val)
            if status_val:
                TodoThisYear.objects.filter(id=task_id).update(status=status_val)
            if finish_val:
                TodoThisYear.objects.filter(id=task_id).update(finished=finish_val)
            return redirect('todo_yearly')

    else:
        plan_y_form = TodoThisYearForm()
        tasks_year = TodoThisYear.objects.all()
        finish_val = get_finished_val_num()
        task_ids = TodoThisYear.objects.order_by().values_list('id', flat=True).distinct()
        exe_status = get_execute_status()
        import_all = get_important_weight()
        return render(request, "todo_yearly.html", {'year_form': plan_y_form,
                                                    'tasks_year': tasks_year,
                                                    'task_ids': task_ids,
                                                    'status_all': exe_status,
                                                    'importance_all': import_all,
                                                    'finish_vals': finish_val, })
