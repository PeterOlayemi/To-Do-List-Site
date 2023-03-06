from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Image1(models.Model):
    image1 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image2(models.Model):
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image3(models.Model):
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image4(models.Model):
    image4 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image5(models.Model):
    image5 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image6(models.Model):
    image6 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image7(models.Model):
    image7 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image8(models.Model):
    image8 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image9(models.Model):
    image9 = models.ImageField(upload_to='images/', blank=True, null=True)
    
class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

class Todo(models.Model):
    task=models.CharField(max_length=100, help_text='Enter Your Task Name')
    short_description=models.TextField(help_text='Optional. Add A Short Description Of Your Task Or Deadline', blank=True, null=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=100, default='Ongoing')
    date_added=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
