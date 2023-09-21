from django.db import models

# Create your models here.
class Tutorials(models.Model):
    title = models.CharField(max_length=25, blank=False, default='')
    description = models.CharField(max_length=25, blank=False, default='')
    published = models.BooleanField(default=False)