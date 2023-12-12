from django.db import models

# Create your models here.
class Books(models.Model):
    access_no = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='AVAILABLE')
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return(f"{self.access_no} {self.title}")	