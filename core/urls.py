from django.urls import path
from .views import *
urlpatterns = [
    
    path('account', dashboard, name='dashboard'), 

    path('account/departments/', departments, name='departments'),
    path('account/department/create/', department_create, name='department_create'),
    path('account/department/<slug:slug>/edit/', department_update, name='department_update'),
    path('account/department/<slug:slug>/delete/', department_delete, name='department_delete'),
    
]