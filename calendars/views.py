# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Entry
from .forms import EntryForm
from django.http import HttpResponseRedirect


# Create your views here.
def index1(request):
    entries = Entry.objects.all()
    return render(request,'calendars/index1.html',{'entries': entries})

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
