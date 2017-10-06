# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Permission(models.Model):
    name = models.ChartField(max_length=32)
    description = models.ChartField(max_length=64)

class Category(models.Model):
    name = models.ChartField(max_length=32)
    description = models.ChartField(max_length=64)

class Group(models.Model):
    name = models.ChartField(max_length=32)
    description = models.ChartField(max_length=64)
    red = models.ChartField(max_length=64)
    subnet = models.ChartField(max_length=128)

class Person(models.Modal):
    name = models.ChartField(max_length=32)
    description = models.ChartField(max_length=64)
    ip = models.ChartField(max_length=64)
