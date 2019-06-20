from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('index', views.index, name='index'),
     path('addstudent', views.addstudent, name='addstudent'),
     path('si', views.si, name='si'),
]