# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main.models import *
# Register your models here.

admin.site.register(Group)
admin.site.register(Permission)
admin.site.register(Person)
admin.site.register(PermissionGroup)
admin.site.register(CategoryGroup)
admin.site.register(Category)
