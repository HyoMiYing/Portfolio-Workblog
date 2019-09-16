from django.urls import path

from . import views

app_name = 'workblog'
urlpatterns = [
    path('', views.index, name="index"),
    path('projects', views.projects, name="projects"),
    path('blog', views.blog, name='blog'),
]