from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = RichTextField(blank=True,null=True,max_length=2000)
    #summary = models.CharField(max_length=500)
