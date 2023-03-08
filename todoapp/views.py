from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from .models import User, Todo
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
    dataset = Todo.objects.all().filter(owner=request.user, status='Completed').order_by('-date_updated')
    context={'dataset':dataset}
    return render(request, 'andtodo.html', context)

@login_required
def todo(request):
    dataset = Todo.objects.all().filter(owner=request.user, status='Ongoing').order_by('-date_updated')
    context={'dataset':dataset}
    return render(request, 'todo.html', context)

@login_required
def addtodo(request):
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
    context = {'form': form}
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
    return render(request, 'index.html')
