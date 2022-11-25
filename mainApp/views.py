from django.shortcuts import render
from .models import *
def home(request):
    context  = {

    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')
def projects(request):
    remodeling = Project.objects.filter(category__icontains='Remodeling')
    construction = Project.objects.filter(category__icontains='Remodeling')
    design = Project.objects.filter(category__icontains='Remodeling')
    repairs = Project.objects.filter(category__icontains='Remodeling')

    context = {
        'remodeling': remodeling,
        'construction': construction,
        'design': design,
        'repairs': repairs,
    }
    return render(request, 'projects.html', context)
def service_details(request):
    return render(request, 'service-details.html')
def blog_details(request):
    return render(request, 'blog-details.html')
def project_details(request):
    return render(request, 'project-details.html')
