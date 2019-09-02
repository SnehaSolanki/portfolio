from django.urls import path

from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:blog_id>', views.detail, name='detail'),
]
