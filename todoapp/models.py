from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

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
