from django.contrib import admin
from .models import User, Todo, Image1, Image2, Image3, Image4, Image5, Image6, Image7, Image8, Image9

# Register your models here.

admin.site.register(Image1)

admin.site.register(Image2)

admin.site.register(Image3)

admin.site.register(Image4)

admin.site.register(Image5)

admin.site.register(Image6)

admin.site.register(Image7)

admin.site.register(Image8)

admin.site.register(Image9)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name', 'email')

admin.site.register(User, UserAdmin)

class TodoAdmin(admin.ModelAdmin):
    list_display = ('task','status','owner', 'date_updated')

admin.site.register(Todo, TodoAdmin)
