# -*_ coding: utf-8 -*-
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, HttpResponse
from sfxRelease.models import SoftwareRelease, FirmwareRelease, AppRelease, SoftwareBranch, FirmwareType, AppType
from sfxProduct.models import Product
from tcProject.models import ProjectCategory, GeneralTcNote, ReleaseTcSummary, TcStatus, TcProject
from .forms import SignupForm, SoftwareReleaseForm, FirmwareReleaseForm, AppReleaseForm,\
    ReleaseTcSummaryForm, GeneralTcNoteForm


def home(request):
    sw_releases = SoftwareRelease.objects.all()
    fw_releases = FirmwareRelease.objects.all()
    app_release = AppRelease.objects.all()
    tc_categories = ProjectCategory.objects.all()
    tc_projects = TcProject.objects.all()
    products = Product.objects.all()
    sw_branches = SoftwareBranch.objects.all()
    fw_branches = FirmwareType.objects.all()
    app_branches = AppType.objects.all()

    sw_tc_summary = ReleaseTcSummary.objects.all()
    if sw_tc_summary:
        sw_tc_summary = sw_tc_summary[0]
        re_tc_projects = GeneralTcNote.objects.filter(sw_revision=sw_tc_summary.sw_revision.id)
    else:
        sw_tc_summary = None
        re_tc_projects = None

    return render(request, 'home.html', {'sw_releases': sw_releases,
                                         'fw_releases': fw_releases,
                                         'app_releases': app_release,
                                         'sw_tc_summary': sw_tc_summary,
                                         'tc_categories': tc_categories,
                                         'tc_projects': tc_projects,
                                         're_tc_projects': re_tc_projects,
                                         'products': products,
                                         'signup': SignupForm,
                                         'sw_new': SoftwareReleaseForm,
                                         'fw_new': FirmwareReleaseForm,
                                         'app_new': AppReleaseForm,
                                         'sw_branches': sw_branches,
                                         'fw_branches': fw_branches,
                                         'app_branches': app_branches})


def release_add(request, rel_type):
    if request.method == 'POST':
        form = ''
        if rel_type == 'sw_release':
            form = SoftwareReleaseForm(request.POST)
        elif rel_type == 'fw_release':
            form = FirmwareReleaseForm(request.POST)
        elif rel_type == 'app_release':
            form = AppReleaseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        HttpResponse("Oops. This is an invalid request")


def get_sum_info(request):
    if request.POST.get('sw_revision'):
        sw_revision = request.POST.get('sw_revision', '')
        schedule_start = request.POST.get('start_date', '')
        schedule_end = request.POST.get('end_date', '')
        sw_release_obj = SoftwareRelease.objects.get(revision=sw_revision)

        if sw_release_obj:
            if schedule_start or schedule_end:
                tc_summary_obj = ReleaseTcSummary.objects.filter(sw_revision=sw_release_obj.id)

                if tc_summary_obj:
                    if schedule_start:
                        tc_summary_obj.update(schedule_start=schedule_start)
                    if schedule_end:
                        tc_summary_obj.update(schedule_end=schedule_end)
                else:
                    form = ReleaseTcSummaryForm()  # if no () will report self position needed
                    tc_summary = form.save(commit=False)
                    tc_summary.sw_revision = sw_release_obj
                    tc_summary.schedule_start = schedule_start if schedule_start else schedule_end
                    tc_summary.schedule_end = schedule_end if schedule_end else schedule_start
                    tc_summary.status = TcStatus.objects.get(name='Not-Started')  # Same with default valuse
                    tc_summary.save()

            elif not ReleaseTcSummary.objects.get(sw_revision=sw_release_obj.id):
                form = ReleaseTcSummaryForm()
                tc_summary = form.save(commit=False)
                tc_summary.sw_revision = sw_release_obj
                tc_summary.status = TcStatus.objects.get(name='Not-Started')  # Same with default valuse
                tc_summary.save()
        else:
            return HttpResponse("No data found about " + sw_revision)

        sw_releases = SoftwareRelease.objects.all()
        fw_releases = FirmwareRelease.objects.all()
        app_release = AppRelease.objects.all()
        tc_categories = ProjectCategory.objects.all()
        tc_projects = TcProject.objects.all()
        products = Product.objects.all()
        sw_branches = SoftwareBranch.objects.all()
        fw_branches = FirmwareType.objects.all()
        app_branches = AppType.objects.all()
        sw_tc_summary = ReleaseTcSummary.objects.get(sw_revision=sw_release_obj.id)
        re_tc_projects = GeneralTcNote.objects.filter(sw_revision=sw_tc_summary.sw_revision.id)

        return render(request, 'home.html', {'sw_releases': sw_releases,
                                             'fw_releases': fw_releases,
                                             'app_releases': app_release,
                                             'sw_tc_summary': sw_tc_summary,
                                             'tc_categories': tc_categories,
                                             'tc_projects': tc_projects,
                                             're_tc_projects': re_tc_projects,
                                             'products': products,
                                             'signup': SignupForm,
                                             'sw_new': SoftwareReleaseForm,
                                             'fw_new': FirmwareReleaseForm,
                                             'app_new': AppReleaseForm,
                                             'sw_branches': sw_branches,
                                             'fw_branches': fw_branches,
                                             'app_branches': app_branches})
    else:
        return HttpResponse('Oops. Not a valid request')


def create_testing_notes(request, sw_revision):
    if request.method == 'POST':
        projects = TcProject.objects.all()
        tc_prjs = ''
        if projects:
            tc_prjs = [project for project in projects if request.POST.get(project.name, '') == 'on']

        for project in tc_prjs:
            form = GeneralTcNoteForm()
            note = form.save(commit=False)
            note.project = project
            note.sw_revision = SoftwareRelease.objects.get(revision=sw_revision)
            note.tc_status = TcStatus.objects.get(name='Not-Started')
            note.owner = request.user
            note.save()

        return redirect('home')
    else:
        return HttpResponse('Oops. Not a valid request')


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
        return HttpResponse("Oops. It's not a valid request")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            msg = "Oops...You are not signed up"
            return HttpResponse(msg)
    else:
        return redirect('home')


def user_logout(request):
    logout(request)
    return redirect('home')
