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
    path('account/job/<slug:slug>/delete/', job_delete, name='job-delete'),

    path('account/applications/', ApplicationListView.as_view(), name='application-list'),
    path('account/applications/<slug:slug>', view_application, name='view_application'),

    path('acccont/application/department/<slug:slug>', view_application_job, name='view_application_job'),
   
    path('account/resumes/', ResumeListView.as_view(), name='resume-list'),
    path('account/resumes/<slug:slug>', view_resume, name='view_resume'),

    path('account/messages/', MessageListView.as_view(), name='message-list'),
    path('account/message/<slug:slug>', view_message, name='view_message'),


    # path('account/applications/create/', ApplicationCreateView.as_view(), name='application-create'),
    # path('account/applications/<slug:slug>/update/', ApplicationUpdateView.as_view(), name='application-update'),
    # path('account/applications/<slug:slug>/delete/', ApplicationDeleteView.as_view(), name='application-delete'),
]