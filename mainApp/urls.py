from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('services/', services, name='services'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('service-details/', service_details, name='service-details'),
    path('blog-details/', blog_details, name='blog-details'),
    path('project-details/', project_details, name='project-details'),

    ]