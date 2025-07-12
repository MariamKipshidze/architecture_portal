from django.shortcuts import render, get_object_or_404
from project.models import Project


def project_list(request):
    projects = Project.objects.filter(is_published=True).order_by('-start_date')
    return render(request, 'project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})
