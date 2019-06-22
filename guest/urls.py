from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('index', views.index, name='index'),
     path('addstudent', views.addstudent, name='addstudent'),
     path('viewstudent', views.viewstudent, name='viewstudent'),
     path('Editstudent', views.Editstudent, name='Editstudent'),
     path('updatestudent', views.updatestudent, name='updatestudent'),
     path('Deletestudent', views.Deletestudent, name='Deletestudent'),
     path('loginstudent', views.loginstudent, name='loginstudent'),
     path('si', views.si, name='si'),
]