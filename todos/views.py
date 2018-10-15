# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect

from .models import Todo

# Create your views here.
def index(request):
    todos= Todo.objects.all()[:10]
    context ={
        'todos':todos
    }
    return render(request, 'index.html',context)

def details(request,id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }
    return render(request, 'details.html',context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo =Todo(title=title, text=text)
        todo.save()

        return HttpResponseRedirect('/todos')
    else:
        return render(request, 'add.html')

def delete(request, id):
    if request.method == 'DELETE':
        entry = get_object_or_404(Todo, id=id)
        entry.delete()

    return HttpResponseRedirect('/todos')
