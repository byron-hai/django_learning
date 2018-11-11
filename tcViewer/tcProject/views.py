from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.utils.text import slugify
from sfxRelease.models import SoftwareRelease
from .models import GeneralTcNote, TcProject, ProjectCategory
from .forms import TcProjectForm


def testing_projects(request):
    tc_projects = TcProject.objects.all()
    tc_categories = ProjectCategory.objects.all()
    return render(request, 'tc_projects.html', {'tc_categories': tc_categories,
                                                'tc_projects': tc_projects,
                                                'prj_new': TcProjectForm})


def create_new_project(request):
    if request.method == 'POST':
        form = TcProjectForm(request.POST)
        if form.is_valid():
            prj_sub = form.save(commit=False)
            project = TcProject.objects.filter(name=prj_sub.name, category=prj_sub.category)

            if project:
                project.update(slug=slugify(prj_sub.name))
                project.update(category=prj_sub.category)
                project.update(description=prj_sub.description)
                project.update(tc_feature=prj_sub.tc_feature)
            else:
                prj_sub.slug = slugify(prj_sub.name)
                prj_sub.save()

        return redirect('tc_projects')
    return HttpResponse("Not a valid request")


def tc_view(request, sw_revision, tc_name):
    if request.method == 'GET':
        tc_prj = TcProject.objects.get(slug=tc_name)
        sw_release = SoftwareRelease.objects.get(revision=sw_revision)
        tc_notes = GeneralTcNote.objects.filter(project=tc_prj, sw_revision=sw_release)
        tc_notes = tc_notes if tc_notes else None

        return render(request, 'general_test.html', {'tc_notes': tc_notes})
    else:
        return HttpResponse('Oops. Nothing found for your request')


def tc_report(request, sw_revision):
    if request.method == 'GET':
        sw_release = SoftwareRelease.objects.get(revision=sw_revision)
        tc_notes = GeneralTcNote.objects.filter(sw_revision=sw_release)

        return render(request, 'release_report.html', {'tc_notes': tc_notes})
    else:
        return HttpResponse('Oops. Nothing found')
