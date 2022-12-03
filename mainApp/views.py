from django.shortcuts import render, redirect
from .models import *
def home(request):
    slider = Slider.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        hi = Message(name=name, email=email, subject=subject, message=message)
        hi.save()
        return redirect('home')

    remodeling = Project.objects.filter(category__icontains='Remodeling')[:3]
    construction = Project.objects.filter(category__icontains='Construction')[:3]
    design = Project.objects.filter(category__icontains='Design')[:3]
    repairs = Project.objects.filter(category__icontains='Repairs')[:3]
    testimonial = Testimonial.objects.all()
    recent_blog = Blog.objects.all().order_by('-date')[:3]
    constructions = Construction.objects.all()[:4]
    services = Service.objects.all()

    modisit = Feature.objects.filter(category__icontains='Modisit')
    praesenti = Feature.objects.filter(category__icontains='Praesenti')
    explica = Feature.objects.filter(category__icontains='Explica')
    nostrum = Feature.objects.filter(category__icontains='Nostrum')

    if request.method == 'POST':
        email = request.POST.get('email')
        us = NewsLetter(email=email)
        us.save()
        return redirect('home')


    context  = {
        'slider': slider,
        'remodeling': remodeling,
        'construction': construction,
        'design': design,
        'repairs': repairs,
        'constructions': constructions,
        'services': services,

        'modisit': modisit,
        'praesenti': praesenti,
        'explica': explica,
        'nostrum': nostrum,

        'testimonials': testimonial,

        'rblog': recent_blog

    }
    return render(request, 'index.html', context)
def about(request):
    abouts = About.objects.all()
    teams = OurTeam.objects.all()
    testimonial = Testimonial.objects.all()
    count = Project.objects.all().count()
    context = {
        'abouts': abouts,
        'teams': teams,
        'testimonials': testimonial,
        'count': count,
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
    recent_blog = Blog.objects.all().order_by('-date')[:10]
    context = {
        'bdetails': blog_detail,
        'r_blog': recent_blog,
    }
    return render(request, 'blog-details.html', context)
def contact(request):
    contact = Contact.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ci = Message(name=name, email=email, subject=subject, message=message)
        ci.save()
        return redirect('contact')
    return render(request, 'contact.html', {'contacts': contact})
def services(request):
    services = Service.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        'services': services,
        'testimonials': testimonial,
    }
    return render(request, 'services.html', context)
def service_details(request,pk):
    services = Service.objects.get(pk=pk)
    return render(request, 'service-details.html', {'services': services})
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

# def newsLetter(request):
#
#         return render(request, 'index.html')