from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages as msg


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




def dashboard(request):
    return render(request, 'backend/dashboard.html')