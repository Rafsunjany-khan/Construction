from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=800)
    sub_title = models.CharField(max_length=800)
    slide = models.ImageField(upload_to='slider_image')

    def __str__(self):
        return self.title
class Project(models.Model):
    CHOICE_PROJECT =(
        ('Remodeling','Remodeling'),
        ('Construction', 'Construction'),
        ('Repairs', 'Repairs'),
        ('Design', 'Design'),
    )
    category = models.CharField(max_length=250, choices=CHOICE_PROJECT, default='Remodeling')
    image = models.ImageField(upload_to='projects')
    title = models.CharField(max_length=800)
    details = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    date = datetime.now()
    name = models.CharField(max_length=800)
    designation = models.CharField(max_length=800)
    image = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=800)
    content = RichTextField()

    def __str__(self):
        return self.name
class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=800)

    def __str__(self):
        return self.email
class Testimonial(models.Model):
    image = models.ImageField(upload_to='team')
    name = models.CharField(max_length=800)
    designations = models.CharField(max_length=800)
    message = models.CharField(max_length=800)

    def __str__(self):
        return self.name
class Message(models.Model):
    name = models.CharField(max_length=800)
    email = models.EmailField()
    subject = models.CharField(max_length=800)
    message = RichTextField()


    def __str__(self):
        return self.email


