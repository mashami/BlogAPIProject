import email
from django.db import models

# Create your models here.


class Articles(models.Model):
    titel=models.CharField(max_length=100)
    auther=models.CharField(max_length=100)
    image=models.ImageField(null=True,blank=False, upload_to="blog")
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titel
    
    
    
    