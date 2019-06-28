from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('home', views.index, name='index'),
     path('login', views.login, name='login'),
     path('dashboard', views.dashboard, name='dashboard'),
     path('cat', views.addcat, name='addcat'),
     path('subcat', views.subcat, name='subcat'),
     path('addsubcat', views.addsubcat, name='addsubcat'),
    
     path('logout', views.logout, name='logout')
]