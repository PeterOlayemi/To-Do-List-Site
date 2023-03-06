from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from .models import User, Todo, Image1, Image2, Image3, Image4, Image5, Image6, Image7, Image8, Image9
from .forms import RegisterForm, TodoForm

# Create your views here.

def term(request):
    return render(request, 'term.html')

def privacy(request):
    return render(request, 'privacy.html')

@login_required
def delete(request, id):
    dataset=Todo.objects.get(id=id)
    dataset.delete()
    return HttpResponseRedirect(reverse('todo'))

@login_required
def changer(request, id):
    air =Todo.objects.filter(owner=request.user).get(id=id)
    air.status='Ongoing'
    air.save()
    return redirect('andtodo')

@login_required
def change(request, id):
    air =Todo.objects.filter(owner=request.user).get(id=id)
    air.status='Completed'
    air.save()
    return redirect('todo')

@login_required
def deletetodo(request, id):
    dataset=Todo.objects.get(id=id)
    dataset.delete()
    return HttpResponseRedirect(reverse('andtodo'))

@login_required
def andtodo(request):
    image1=Image1.objects.all()
    image2=Image2.objects.all()
    image5=Image5.objects.all()
    dataset = Todo.objects.all().filter(owner=request.user, status='Completed').order_by('-date_updated')
    context={'dataset':dataset, 'image1':image1, 'image2':image2, 'image5':image5, }
    return render(request, 'andtodo.html', context)

@login_required
def todo(request):
    image1=Image1.objects.all()
    image2=Image2.objects.all()
    image5=Image5.objects.all()
    dataset = Todo.objects.all().filter(owner=request.user, status='Ongoing').order_by('-date_updated')
    context={'dataset':dataset, 'image1':image1, 'image2':image2, 'image5':image5, }
    return render(request, 'todo.html', context)

@login_required
def addtodo(request):
    image1=Image1.objects.all()
    image2=Image2.objects.all()
    image5=Image5.objects.all()
    if request.method != 'POST':
        form = TodoForm()
    else:
        # Process completed form.
        form = TodoForm(request.POST)
        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.owner=request.user
            new_student.save()
            return HttpResponseRedirect(reverse('todo'))
    context = {'form': form, 'image1':image1, 'image2':image2, 'image5':image5,}
    return render(request, 'addtodo.html', context)

class register(CreateView):
    model = User  
    form_class = RegisterForm
    template_name= 'register.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('login')

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def home(request):
    image1=Image1.objects.all()
    image2=Image2.objects.all()
    image3=Image3.objects.all()
    image4=Image4.objects.all()
    image5=Image5.objects.all()
    image6=Image6.objects.all()
    image7=Image7.objects.all()
    image8=Image8.objects.all()
    image9=Image9.objects.all()
    return render(request, 'index.html', {'image1':image1, 'image2':image2, 'image3':image3, 'image4':image4, 'image5':image5, 'image6':image6, 'image7':image7, 'image8':image8, 'image9':image9})