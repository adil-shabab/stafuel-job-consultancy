from django.db import models
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