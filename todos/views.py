# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect

from .models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    todos= Todo.objects.filter(author= request.user)[:10]
    context ={
        'todos':todos
    }
    return render(request, 'index.html',context)

@login_required
def details(request,id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }
    return render(request, 'details.html',context)

@login_required
def add(request):
    if(request.method == 'POST'):
        author= request.user,
        title = request.POST['title']
        text = request.POST['text']

        todo =Todo(title=title, text=text,author= request.user)
        todo.save()

        return HttpResponseRedirect('/todos')
    else:
        return render(request, 'add.html')

@login_required
def delete(request, id):
    if request.method == 'DELETE':
        entry = get_object_or_404(Todo, id=id)
        entry.delete()

    return HttpResponseRedirect('/todos')
