from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.core.exceptions import ValidationError
import os



def validate_pdf(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Only PDF files are allowed.')



# Create your models here.
class Department(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]


    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    openings = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while Department.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super(Department, self).save(*args, **kwargs)

    def __str__(self):
        return self.name




class Job(models.Model):


    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance'),
    ]

    EXPERIENCE_CHOICES = [
        ('0-1', '0-1 years'),
        ('1-2', '1-2 years'),
        ('2-3', '2-3 years'),
        ('3-4', '3-4 years'),
        ('4-5', '4-5 years'),
        ('5+', '5+ years'),
    ]


    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    title = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    salary = models.CharField(max_length=255)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE_CHOICES, default='full time')
    experience = models.CharField(max_length=3, choices=EXPERIENCE_CHOICES)
    job_description = models.TextField()
    skills_required = RichTextField()
    slug = models.SlugField(unique=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='active')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            counter = 1
            while Job.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super(Job, self).save(*args, **kwargs)


    def __str__(self):
        return self.title


    
class Application(models.Model):
    EXPERIENCE_CHOICES = [
        ('0-1', '0-1 years'),
        ('1-2', '1-2 years'),
        ('2-3', '2-3 years'),
        ('3-4', '3-4 years'),
        ('4-5', '4-5 years'),
        ('5+', '5+ years'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    experience = models.CharField(max_length=3, choices=EXPERIENCE_CHOICES)
    skills = RichTextField()
    resume = models.FileField(upload_to='resumes/', validators=[validate_pdf])
    slug = models.SlugField(unique=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while Application.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super(Application, self).save(*args, **kwargs)



    def __str__(self):
        return f'{self.name} - {self.job.title}'




class Resume(models.Model):

    EXPERIENCE_CHOICES = [
        ('0-1', '0-1 years'),
        ('1-2', '1-2 years'),
        ('2-3', '2-3 years'),
        ('3-4', '3-4 years'),
        ('4-5', '4-5 years'),
        ('5+', '5+ years'),
    ]
    
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=14)
    experience = models.CharField(max_length=3, choices=EXPERIENCE_CHOICES)
    skills = RichTextField()
    resume = models.FileField(upload_to='resumes/', validators=[validate_pdf])
    job_title = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + '-' + self.job_title)
            original_slug = self.slug
            counter = 1
            while Resume.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super(Resume, self).save(*args, **kwargs)




    def __str__(self):
        return self.name