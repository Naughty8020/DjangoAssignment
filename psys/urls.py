# psys/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('main/', views.main, name='main'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('customers/', views.customers, name='customers'),
    path('customer_list/', views.customer_list, name='customer_list'),
    path('customer_crate/', views.customer_create, name='customer_create'),
    path('customer_update/<str:pk>/', views.customer_update, name='customer_update'),
    path('customer_delete/<str:pk>/', views.customer_delete, name='customer_delete'),
    path('orders_list/', views.orders_list, name='orders_list'),
    path('search/', views.customer_list, name='customer_search') 
]
