from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('services/', services, name='services'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('blog-details/<pk>', blog_details, name='blog-details'),
    path('project-details/<pk>', project_details, name='project-details'),
    path('service-details/<pk>', service_details, name='service-details'),

]