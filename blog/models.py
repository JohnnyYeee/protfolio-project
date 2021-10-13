from django.db import models

# Create your models here.

#1create model, adding to setting,migrate1 and 2 ,admin

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

