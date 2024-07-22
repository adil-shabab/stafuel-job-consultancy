from django.shortcuts import render
from core.models import *

# Create your views here.
def home(request):
    departments = Department.objects.filter(status = 'active')
    jobs = Job.objects.filter(status = 'active')
    context = {
        'departments': departments,
        'jobs' : jobs,
    }
    return render(request, 'frontend/home.html', context)