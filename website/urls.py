from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'), 
    path('about', about, name='about'), 
    path('jobs', jobs, name='jobs'), 
    path('blogs', blogs, name='blogs'), 
    path('blogs/title', single_blog, name='single_blog'), 

]