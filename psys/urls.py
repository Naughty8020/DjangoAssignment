# psys/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('main/', views.main, name='main'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    
]
