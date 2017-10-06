# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Permission(models.Model):
    name = models.ChartField(max_length=32)
    description = models.ChartField(max_length=64)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class Category(models.Model):
    name = models.ChartField(max_length=32)
    description = models.ChartField(max_length=64)


class Group(models.Model):
    name = models.ChartField(max_length=32)
    description = models.ChartField(max_length=64)
    red = models.ChartField(max_length=64)
    subnet = models.ChartField(max_length=128)
    persmission = GenericRelation(persmission)

class Person(models.Modal):
    name = models.ChartField(max_length=32)
    description = models.ChartField(max_length=64)
    ip = models.ChartField(max_length=64)
    persmission = GenericRelation(persmission)
