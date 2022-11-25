from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')
def projects(request):
    return render(request, 'projects.html')
def service_details(request):
    return render(request, 'service-details.html')
def blog_details(request):
    return render(request, 'blog-details.html')
def project_details(request):
    return render(request, 'project-details.html')
