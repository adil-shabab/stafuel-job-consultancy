from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages as msg
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count



# Create your views here.


def departments(request):
    departments = Department.objects.all()
    return render(request, 'backend/departments.html', {'departments': departments})

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


def department_delete(request, slug):
    department = get_object_or_404(Department, slug=slug)
    department.delete()
    msg.success(request,"Department Deleted Successfully")
    return redirect('departments')





class JobListView(ListView):
    model = Job
    template_name = 'backend/jobs.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Job.objects.annotate(application_count=Count('application')).order_by('-created_at')

class JobCreateView(CreateView):
    model = Job
    form_class = JobForm
    template_name = 'backend/job-form.html'
    success_url = reverse_lazy('job-list')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        response = super().form_valid(form)
        msg.success(self.request, 'Job created successfully!')
        return response

class JobUpdateView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'backend/job-form.html'
    success_url = reverse_lazy('job-list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        response = super().form_valid(form)
        msg.success(self.request, 'Job updated successfully!')
        return response



def job_delete(request, slug):
    job = get_object_or_404(Job, slug=slug)
    job.delete()
    msg.success(request,"Job Deleted Successfully")
    return redirect('job-list')




    
class ApplicationListView(ListView):
    model = Application
    template_name = 'backend/applications.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.all().order_by('-created_at')

        
def view_application(request, slug):
    application = Application.objects.get(slug=slug)
    return render(request, 'backend/application-view.html', {'application': application})

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




class ResumeListView(ListView):
    model = Application
    template_name = 'backend/resumes.html'
    context_object_name = 'resumes'

    def get_queryset(self):
        return Resume.objects.all().order_by('-created_at')

        
def view_resume(request, slug):
    resume = Resume.objects.get(slug=slug)
    return render(request, 'backend/resume-view.html', {'resume': resume})


def dashboard(request):
    return render(request, 'backend/dashboard.html')