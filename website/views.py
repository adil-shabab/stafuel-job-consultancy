from django.shortcuts import render, redirect
from core.models import *
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages as msg


# Create your views here.
def home(request):
    departments = Department.objects.filter(status = 'active')
    jobs = Job.objects.filter(status = 'active')
    context = {
        'departments': departments,
        'jobs' : jobs,
    }
    return render(request, 'frontend/home.html', context)



def jobs(request):
    jobs = Job.objects.all()
    departments = Department.objects.all()

    query = request.GET.get('q')
    location = request.GET.get('location')
    department_id = request.GET.get('department')

    if query:
        jobs = jobs.filter(title__icontains=query)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if department_id:
        jobs = jobs.filter(department_id=department_id)

    context = {
        'jobs': jobs,
        'departments': departments,
        'query': query,
        'location': location,
        'department_id': department_id,
    }
    return render(request, 'frontend/jobs.html', context)




def filter_jobs(request):
    jobs = Job.objects.all()
    
    job_type = request.GET.get('job_type')
    experience = request.GET.get('experience')
    q = request.GET.get('q')
    location = request.GET.get('location')
    department = request.GET.get('department')

    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if experience:
        jobs = jobs.filter(experience=experience)
    if q:
        jobs = jobs.filter(title__icontains=q)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if department:
        jobs = jobs.filter(department_id=department)
    
    job_count = jobs.count()
    html = render_to_string('frontend/include/job_list.html', {'jobs': jobs})
    
    return JsonResponse({'html': html, 'count': job_count})






def about(request):
    return render(request, 'frontend/about.html')


def blogs(request):
    return render(request, 'frontend/blogs.html')


def single_blog_1(request):
    return render(request, 'frontend/blog-detail-1.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message_text = request.POST['message']
        mobile = request.POST['mobile']
        
        # Create a new Message object and save it
        message = Message(
            name=name,
            email=email,
            subject=subject,
            message=message_text,
            number=mobile
        )
        message.save()
        msg.success(request, "Message Sent Successfully")
        
        # Redirect to a success page or show a success message
        return redirect('contact')
    
    context = {}
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