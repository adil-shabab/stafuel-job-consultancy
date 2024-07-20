from django import forms
from .models import *




class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'icon', 'openings', 'status']




class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'department', 'location', 'salary', 'job_type', 'experience', 'job_description', 'skills_required', 'status']