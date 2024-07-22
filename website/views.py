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


def about(request):
    context = {

    }
    return render(request, 'frontend/about.html', context)


def jobs(request):
    context = {

    }
    return render(request, 'frontend/jobs.html', context)

def blogs(request):
    context = {

    }
    return render(request, 'frontend/blogs.html', context)
def single_blog(request):
    context = {

    }
    return render(request, 'frontend/blog-detail.html', context)


def contact(request):
    context = {

    }
    return render(request, 'frontend/contact.html', context)


def upload_resume(request):
    context = {

    }
    return render(request, 'frontend/resume.html', context)


def application(request, slug):
    job = Job.objects.get(slug=slug)

    context = {
        'job': job
    }
    return render(request, 'frontend/application.html', context)


def terms(request):
    return render(request, 'frontend/terms.html')