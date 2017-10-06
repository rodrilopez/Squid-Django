# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Permission(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)


class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)


class Group(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    red = models.CharField(max_length=64)
    subnet = models.CharField(max_length=128)
    persmission = GenericRelation(Permission)

class Person(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    ip = models.CharField(max_length=64)
    permission = GenericRelation(Permission)
