# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse
from .forms import PermissionForm, CategoryForm
from .models import *
import squid

def home(request):
    form_permission = PermissionForm()
    form_category = CategoryForm()
    permisos = Permission.objects.all()
    categorys = Category.objects.all()
    aulas = Group.objects.all()
    persons = Person.objects.all()
    return render(request, 'index.html', {'form_permission':form_permission,
                                          'form_category':form_category,
                                          'permisos':permisos,
                                          'categorys':categorys,
                                          'aulas':aulas,
                                          'persons':persons,   })
def createPerm(request):
    if request.method == 'POST':
        perm = Permission()
        form = PermissionForm(request.POST, instance=perm)
        print form.errors
        if form.is_valid():
            perm = form.save(commit=False)
            perm.save()
    return redirect(reverse('main:index'),request)

def createCategory(request):
    if request.method == 'POST':
        category  = Category()
        form = CategoryForm(request.POST, instance=category)
        print form.errors
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
    return redirect(reverse('main:index'),request)


def createPerson(request):
    if request.method == 'POST':
        data = dict(request.POST)
        person = Person()
        person.name = data['person_name'][0]
        person.description = data['person_description'][0]
        person.ip = data['person_ip'][0]
        person.save()
        try:
            if data['person_category']:
                for x in data['person_category']:
                    cat = Category.objects.get(id=x)
                    group = CategoryGroup(category=cat,content_object=person)
                    group.save()
        except Exception as e:
            print e
        try:
            if data['person_permission']:
                for x in data['person_permission']:
                    perm = Permission.objects.get(id=x)
                    group = PermissionGroup(permission=perm,content_object=person)
                    group.save()
        except Exception as e:
            print e
    return redirect(reverse('main:index'),request)




def createGroup(request):
    if request.method == 'POST':
        data = dict(request.POST)
        group = Group()
        group.name = data['aula_name'][0]
        group.description = data['aula_description'][0]
        group.red = data['aula_red'][0]
        group.subnet = data['aula_subnet'][0]
        group.save()
        try:
            if data['group_category']:
                for x in data['group_category']:
                    cat = Category.objects.get(id=x)
                    group = CategoryGroup(category=cat,content_object=group)
                    group.save()
        except Exception as e:
            print e
        try:
            if data['group_permission']:
                for x in data['group_permission']:
                    perm = Permission.objects.get(id=x)
                    group = PermissionGroup(permission=perm,content_object=group)
                    group.save()
        except Exception as e:
            print e
    return redirect(reverse('main:index'),request)
