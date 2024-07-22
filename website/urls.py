from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'), 
    path('about', about, name='about'), 
    path('jobs', jobs, name='jobs'), 
    path('blogs', blogs, name='blogs'), 
    path('blogs/title', single_blog, name='single_blog'), 
    path('contact', contact, name='contact'), 
    path('upload/resume', upload_resume, name='upload_resume'), 
    path('jobs/<slug:slug>', application, name='application'), 
    path('terms', terms, name='terms'), 

]