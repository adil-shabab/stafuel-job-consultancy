from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages as msg
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('job-list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        msg.success(self.request, 'Job deleted successfully!')
        return response


def dashboard(request):
    return render(request, 'backend/dashboard.html')