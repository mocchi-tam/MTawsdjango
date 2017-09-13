from django.conf.urls import url
from django.contrib import admin
from aws_eb_docker_django_skeleton.image import views

urlpatterns = [
    url(r'^$', views.ImageList.as_view(), name='list'),
    url(r'^create/$', views.ImageForm.as_view(), name='create'),
]