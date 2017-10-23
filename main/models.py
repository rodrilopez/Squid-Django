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
    permission = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    permission = models.TextField()

    def __str__(self):
        return self.name



class Group(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    red = models.CharField(max_length=64)
    subnet = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField('nombre',max_length=32)
    description = models.CharField(max_length=64)
    ip = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class PermissionGroup(models.Model):
    permission = models.ForeignKey(Permission)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.permission.name


class CategoryGroup(models.Model):
    category = models.ForeignKey(Category)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.category.name
