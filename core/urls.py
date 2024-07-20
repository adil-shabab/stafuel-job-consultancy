from django.urls import path
from .views import *
urlpatterns = [
    
    path('account', dashboard, name='dashboard'), 

    path('account/departments/', departments, name='departments'),
    path('account/department/create/', department_create, name='department_create'),
    path('account/department/<slug:slug>/edit/', department_update, name='department_update'),
    path('account/department/<slug:slug>/delete/', department_delete, name='department_delete'),
    
    path('account/jobs/', JobListView.as_view(), name='job-list'),
    path('account/job/create/', JobCreateView.as_view(), name='job-create'),
    path('account/job/<slug:slug>/update/', JobUpdateView.as_view(), name='job-update'),
    path('account/job/<slug:slug>/delete/', JobDeleteView.as_view(), name='job-delete'),
]