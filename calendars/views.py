# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Entry
from .forms import EntryForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index1(request):
    entries = Entry.objects.all()
    return render(request,'calendars/index1.html',{'entries': entries})

def home(request):
    return render(request,'home.html')

def details_c(request,pk):
    entry = Entry.objects.get(id=pk)

    context = {
        'entry': entry
    }
    return render(request, 'details_c.html',context)

def add_c(request):
    if(request.method == 'POST'):
        form = EntryForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Entry.objects.create(
                name=name,
                date = date,
                description = description,
            ).save()
            return HttpResponseRedirect('/calendars')
    else:
        form = EntryForm()

    return render(request, 'form.html', {'form':form})

def delete_c(request , pk):
    if request.method == 'DELETE':
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()

    return HttpResponseRedirect('/calendars')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
