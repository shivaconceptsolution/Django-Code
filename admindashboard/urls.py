from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('home', views.index, name='index'),
     path('login', views.login, name='login'),
     path('dashboard', views.dashboard, name='dashboard'),
    
     path('logout', views.logout, name='logout')
]