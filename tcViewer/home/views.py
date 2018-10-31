# -*_ coding: utf-8 -*-
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, HttpResponse, get_list_or_404
from django.contrib.auth.models import User
from sfxRelease.models import SoftwareRelease, FirmwareRelease, AppRelease
from sfxProduct.models import Product
from tcProject.models import GeneralTcNote
from tcProject.models import ReleaseTcSummary
from .forms import SignupForm


def home(request):
    if request.method == 'POST':
        sw_release_new = request.POST.get('', '')

    else:
        sw_releases = SoftwareRelease.objects.all()
        fw_releases = FirmwareRelease.objects.all()
        app_release = AppRelease.objects.all()
        sw_tc_summary = ReleaseTcSummary.objects.all()[0]
        tc_projects = GeneralTcNote.objects.all()
        products = Product.objects.all()

        signup_form = SignupForm()
        return render(request, 'home.html', {'sw_releases': sw_releases,
                                             'fw_releases': fw_releases,
                                             'app_releases': app_release,
                                             'sw_tc_summary': sw_tc_summary,
                                             'tc_projects': tc_projects,
                                             'products': products,
                                             'signup': signup_form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        return HttpResponse("")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
    else:
        return redirect('home')


def user_logout(request):
    logout(request)
    return redirect('home')


'''
def tc_view(request, revision, prj_name):
    if request.method == 'POST':
        tc_plan = 'say_hi'
        return render(request, 'general_test.html', {'tc_info': tc_plan})
    else:

        return render(request, 'general_test.html', {'title': prj_name,
                                                     'drv_revision': revision,
                                                     'tc_projects': prj_name})
'''

