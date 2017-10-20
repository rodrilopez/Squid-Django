from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index', home, name='index'),
    url(r'^perm', createPerm, name='create-permission'),
    url(r'^category', createCategory, name='create-category'),
]
