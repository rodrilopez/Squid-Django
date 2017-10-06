from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index', principal, name='index'),
]
