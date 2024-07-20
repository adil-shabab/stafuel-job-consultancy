from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    openings = models.IntegerField()

    def __str__(self):
        return self.name