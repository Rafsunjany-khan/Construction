from django.shortcuts import render
from .models import *
def home(request):
    remodeling = Project.objects.filter(category__icontains='Remodeling')[:3]
    construction = Project.objects.filter(category__icontains='Construction')[:3]
    design = Project.objects.filter(category__icontains='Design')[:3]
    repairs = Project.objects.filter(category__icontains='Repairs')[:3]
    testimonial = Testimonial.objects.all()
    recent_blog = Blog.objects.all()[:3]

    context  = {
        'remodeling': remodeling,
        'construction': construction,
        'design': design,
        'repairs': repairs,

        'testimonials': testimonial,

        'rblog': recent_blog

    }
    return render(request, 'index.html', context)
def about(request):
    testimonial = Testimonial.objects.all()
    context = {
        'testimonials': testimonial,
    }
    return render(request, 'about.html', context)
def blog(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)
def blog_details(request,pk):
    blog_detail = Blog.objects.get(pk=pk)
    recent_blog = Blog.objects.all()[:10]
    context = {
        'bdetails': blog_detail,
        'r_blog': recent_blog,
    }
    return render(request, 'blog-details.html', context)
def contact(request):
    contact = Contact.objects.all()
    return render(request, 'contact.html', {'contacts': contact})
def services(request):
    testimonial = Testimonial.objects.all()
    context = {
        'testimonials': testimonial,
    }
    return render(request, 'services.html', context)
def service_details(request):
    return render(request, 'service-details.html')
def projects(request):
    remodeling = Project.objects.filter(category__icontains='Remodeling')
    construction = Project.objects.filter(category__icontains='Construction')
    design = Project.objects.filter(category__icontains='Design')
    repairs = Project.objects.filter(category__icontains='Repairs')

    context = {
        'remodeling': remodeling,
        'construction': construction,
        'design': design,
        'repairs': repairs,
    }
    return render(request, 'projects.html', context)
def project_details(request,pk):
    project_details = Project.objects.get(pk=pk)
    return render(request, 'project-details.html', {'pdetails': project_details})
