from django.db import models

# Create your models here.

#1create model, adding to setting,migrate1 and 2 ,admin

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

