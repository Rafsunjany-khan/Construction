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
    date = models.DateField()
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
class Service(models.Model):
    title = models.CharField(max_length=800)
    icon = models.ImageField(upload_to='services')
    details = RichTextField()

    def __str__(self):
        return self.title
class Construction(models.Model):
    title = models.CharField(max_length=800)
    image = models.ImageField(upload_to='construction')
    details = RichTextField()

    def __str__(self):
        return self.title
class Feature(models.Model):
    FEATURE_CATEGOARY = (
        ('Modisit','Modisit'),
        ('Praesenti','Praesenti'),
        ('Explica','Explica'),
        ('Nostrum','Nostrum'),
    )
    category = models.CharField(choices=FEATURE_CATEGOARY, max_length=100)
    title = models.CharField(max_length=800)
    image = models.ImageField(upload_to='feature')
    description = RichTextField()

    def __str__(self):
        return self.title

class Mission(models.Model):
    title = models.CharField(max_length=800, null=True, blank=True)
    text = RichTextField()

    def __str__(self):
        if self.title == None:
            return self.title
class Vision(models.Model):
    title = models.CharField(max_length=800, null=True, blank=True)
    text = RichTextField()

    def __str__(self):
        return self.title
class Goal(models.Model):
    title = models.CharField(max_length=800, null=True, blank=True)
    text = RichTextField()

    def __str__(self):
        return self.title
class About(models.Model):
    title = models.CharField(max_length=800)
    sub_title = models.CharField(max_length=800)
    establish_year = models.CharField(max_length=100)
    details = RichTextField()
    image = models.ImageField(upload_to='about')
    video_embed = models.URLField(max_length=200)

    def __str__(self):
        return self.title
class OurTeam(models.Model):
    image = models.ImageField(upload_to='ourTeam')
    name = models.CharField(max_length=800)
    designation = models.CharField(max_length=200)
    message = models.CharField(max_length=800)
    twitter_link = models.URLField(max_length=200)
    facebook_link = models.URLField(max_length=200)
    instagram_link = models.URLField(max_length=200)
    linkedin_link = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class NewsLetter(models.Model):
    email = models.EmailField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.email

