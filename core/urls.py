from django.urls import path
from .views import *
urlpatterns = [
    
    path('', dashboard, name='dashboard'), 
    path('login', login, name='login'), 
    path('logout', logout_user, name='logout'), 

    path('departments/', departments, name='departments'),
    path('department/create/', department_create, name='department_create'),
    path('department/<slug:slug>/edit/', department_update, name='department_update'),
    path('department/<slug:slug>/delete/', department_delete, name='department_delete'),
    
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('job/create/', JobCreateView.as_view(), name='job-create'),
    path('job/<slug:slug>/update/', JobUpdateView.as_view(), name='job-update'),
    path('job/<slug:slug>/delete/', job_delete, name='job-delete'),

    path('applications/', ApplicationListView.as_view(), name='application-list'),
    path('applications/<slug:slug>', view_application, name='view_application'),

    path('acccont/application/department/<slug:slug>', view_application_job, name='view_application_job'),
   
    path('resumes/', ResumeListView.as_view(), name='resume-list'),
    path('resumes/<slug:slug>', view_resume, name='view_resume'),

    path('messages/', MessageListView.as_view(), name='message-list'),
    path('message/<slug:slug>', view_message, name='view_message'),


    # path('applications/create/', ApplicationCreateView.as_view(), name='application-create'),
    # path('applications/<slug:slug>/update/', ApplicationUpdateView.as_view(), name='application-update'),
    # path('applications/<slug:slug>/delete/', ApplicationDeleteView.as_view(), name='application-delete'),
]