from django.contrib import admin
from .models import User, Todo

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name', 'email')

admin.site.register(User, UserAdmin)

class TodoAdmin(admin.ModelAdmin):
    list_display = ('task','status','owner', 'date_updated')

admin.site.register(Todo, TodoAdmin)
