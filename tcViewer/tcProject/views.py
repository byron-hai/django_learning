from django.shortcuts import render, redirect
from sfxRelease.models import SoftwareRelease
from .models import GeneralTcNote, TcProject, ProjectCategory
from .forms import TcProjectForm
from django.contrib.auth.models import User


def demo(request):
    msg = 'ddd'
    return render(request, 'general_test.html', {'msg': msg})


def testing_projects(request):
    tc_projects = TcProject.objects.all()
    tc_categories = ProjectCategory.objects.all()
    return render(request, 'tc_projects.html', {'tc_categories': tc_categories,
                                                'tc_projects': tc_projects,
                                                'prj_new': TcProjectForm})


def tc_view(request, revision, prj_name):
    prj_name = prj_name
    tc_project = TcProject.objects.filter(name=prj_name)
    tc_node = GeneralTcNote.objepcts.filter(name=prj_name, sw_revision=revision)
    msg = 'msg'
    return render(request, 'general_test.html', {'msg': msg})
