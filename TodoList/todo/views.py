from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy 
from .models import task
# Create your views here.

class TaskList(ListView):
    model = task
    context_object_name = 'task1'

class TaskDetail(DetailView):
    model =task
    context_object_name = 'task'
    template_name = 'todo/task.html'

class TaskCreate(CreateView):
    model = task
    fields ="__all__"
    success_url = reverse_lazy('task') 

class TaskUpdate(UpdateView):
    model = task
    fields ="__all__"
    success_url = reverse_lazy("task")

class TaskDelete(DeleteView):
    model = task
    context_object_name = 'task'
    success_url = reverse_lazy("task")
