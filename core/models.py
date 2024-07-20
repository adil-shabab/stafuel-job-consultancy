from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


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
            while Department.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super(Job, self).save(*args, **kwargs)


    def __str__(self):
        return self.title