from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages as msg
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def calculate_percentage_change(current, previous):
    if previous == 0:
        return 0 if current == 0 else 100
    return ((current - previous) / previous) * 100

def calculate_percentage(part, whole):
    if whole == 0:
        return 0
    return (part / whole) * 100





def login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            msg.success(request, "Logged In")
            return redirect('dashboard')
            
        else:
            print("Error")
            msg.error(request, 'Invalid Credential')
            return render(request, 'backend/login.html')
    return render(request, 'backend/login.html')


# logout 
@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def departments(request):
    departments = Department.objects.all()
    return render(request, 'backend/departments.html', {'departments': departments})

@login_required(login_url='login')
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            msg.success(request, "Department Created Successfully")
            return redirect('departments')
    else:
        form = DepartmentForm()
    return render(request, 'backend/department_form.html', {'form': form})


@login_required(login_url='login')
def department_update(request, slug):
    department = get_object_or_404(Department, slug=slug)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            msg.success(request, "Department Updated Successfully")
            return redirect('departments')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'backend/department_form.html', {'form': form})


@login_required(login_url='login')
def department_delete(request, slug):
    department = get_object_or_404(Department, slug=slug)
    department.delete()
    msg.success(request,"Department Deleted Successfully")
    return redirect('departments')



class JobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'backend/jobs.html'
    context_object_name = 'jobs'
    login_url = 'login'  # URL to redirect to if the user is not authenticated


    def get_queryset(self):
        return Job.objects.annotate(application_count=Count('application')).order_by('-created_at')


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'backend/job-form.html'
    success_url = reverse_lazy('job-list')
    login_url = 'login'  # URL to redirect to if the user is not authenticated


    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        response = super().form_valid(form)
        msg.success(self.request, 'Job created successfully!')
        return response

class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'backend/job-form.html'
    success_url = reverse_lazy('job-list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    login_url = 'login'  # URL to redirect to if the user is not authenticated


    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        response = super().form_valid(form)
        msg.success(self.request, 'Job updated successfully!')
        return response




@login_required(login_url='login')
def job_delete(request, slug):
    job = get_object_or_404(Job, slug=slug)
    job.delete()
    msg.success(request,"Job Deleted Successfully")
    return redirect('job-list')




class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'backend/applications.html'
    context_object_name = 'applications'
    login_url = 'login'  # URL to redirect to if the user is not authenticated


    def get_queryset(self):
        return Application.objects.all().order_by('-created_at')

        
@login_required(login_url='login')
def view_application(request, slug):
    application = Application.objects.get(slug=slug)
    return render(request, 'backend/application-view.html', {'application': application})


@login_required(login_url='login')
def view_application_job(request, slug):
    job = Job.objects.get(slug=slug)
    applications = Application.objects.filter(job=job)
    return render(request, 'backend/application-job.html', {'applications': applications, 'job': job})

# class ApplicationCreateView(CreateView):
#     model = Application
#     form_class = ApplicationForm
#     template_name = 'backend/application-form.html'
#     success_url = reverse_lazy('application-list')

#     def form_valid(self, form):
#         form.instance.slug = slugify(form.instance.name)
#         response = super().form_valid(form)
#         msg.success(self.request, 'Application created successfully!')
#         return response

# class ApplicationUpdateView(UpdateView):
#     model = Application
#     form_class = ApplicationForm
#     template_name = 'backend/application-form.html'
#     success_url = reverse_lazy('application-list')
#     slug_field = 'slug'
#     slug_url_kwarg = 'slug'

#     def form_valid(self, form):
#         form.instance.slug = slugify(form.instance.name)
#         response = super().form_valid(form)
#         msg.success(self.request, 'Application updated successfully!')
#         return response

# class ApplicationDeleteView(DeleteView):
#     model = Application
#     template_name = 'backend/application_confirm_delete.html'
#     success_url = reverse_lazy('application-list')
#     slug_field = 'slug'
#     slug_url_kwarg = 'slug'

#     def delete(self, request, *args, **kwargs):
#         response = super().delete(request, *args, **kwargs)
#         msg.success(self.request, 'Application deleted successfully!')
#         return response




class ResumeListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'backend/resumes.html'
    context_object_name = 'resumes'
    login_url = 'login'  # URL to redirect to if the user is not authenticated


    def get_queryset(self):
        return Resume.objects.all().order_by('-created_at')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'backend/messages.html'
    context_object_name = 'msgs'
    login_url = 'login'  # URL to redirect to if the user is not authenticated


    def get_queryset(self):
        return Message.objects.all().order_by('-created_at')

        
        
@login_required(login_url='login')
def view_resume(request, slug):
    resume = Resume.objects.get(slug=slug)
    return render(request, 'backend/resume-view.html', {'resume': resume})



@login_required(login_url='login')
def view_message(request, slug):
    message = Message.objects.get(slug=slug)
    return render(request, 'backend/message-view.html', {'message': message})




@login_required(login_url='login')
def dashboard(request):
    today = now().date()
    first_day_of_current_month = today.replace(day=1)
    first_day_of_previous_month = (first_day_of_current_month - timedelta(days=1)).replace(day=1)

    models = [Message, Resume, Application]
    data = {}

    for model in models:
        current_month_count = model.objects.filter(created_at__gte=first_day_of_current_month).count()
        previous_month_count = model.objects.filter(created_at__gte=first_day_of_previous_month, created_at__lt=first_day_of_current_month).count()
        percentage_change = calculate_percentage_change(current_month_count, previous_month_count)
        
        model_name = model.__name__.lower()
        objects = model.objects.all()
        if model_name == 'resume':
            objects = objects[:6]  # Limit to 6 resumes
        
        data[model_name] = {
            'current_month_count': current_month_count,
            'percentage_change': percentage_change,
            'objects': objects
        }

    # Calculate the counts for the chart by department
    departments = Department.objects.all()
    department_data = []
    total_resumes = Resume.objects.count()

    for department in departments:
        resume_count = Resume.objects.filter(department=department).count()
        percentage = calculate_percentage(resume_count, total_resumes)
        department_data.append({
            'name': department.name,
            'resume_count': resume_count,
            'percentage': percentage
        })

    return render(request, 'backend/dashboard.html', {
        'data': data,
        'department_data': department_data,
    })