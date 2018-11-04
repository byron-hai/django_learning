from django.shortcuts import render, redirect
from sfxRelease.models import SoftwareRelease
from .models import GeneralTcNote, TcProject
from django.contrib.auth.models import User
# Create your views here.


def demo(request):
    msg = 'ddd'
    return render(request, 'general_test.html', {'msg': msg})


def tc_view(request, revision, prj_name):
    prj_name = prj_name
    tc_project = TcProject.objects.filter(name=prj_name)
    tc_node = GeneralTcNote.objepcts.filter(name=prj_name, sw_revision=revision)
    msg = 'msg'
    return render(request, 'general_test.html', {'msg': msg})

