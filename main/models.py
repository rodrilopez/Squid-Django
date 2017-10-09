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
    is_white_list = models.BooleanField()
    persmission = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    permission = models.TextField()


class Group(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    red = models.CharField(max_length=64)
    subnet = models.CharField(max_length=128)


class Person(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    ip = models.CharField(max_length=64)


class PermissionGroup(models.Model):
    persmission = models.ForeignKey(Permission)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class CategoryGroup(models.Model):
    category = models.ForeignKey(Category)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
