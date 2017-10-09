# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.template import loader
from .forms import PermissionForm, CategoryForm
# Create your views here.

def principal(request):
    form_permission = PermissionForm()
    form_category = CategoryForm()
    return render(request, 'index.html', {'form_permission':form_permission,
                                          'form_category':form_category})
