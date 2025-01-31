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



class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['job', 'name', 'email', 'mobile_number', 'experience', 'skills', 'resume', 'department']