from django.db import models

# Create your models here.
class Student(models.Model):
    
    name=models.CharField(max_length=100,blank=False,null=True)
    age=models.IntegerField(blank=False,null=True)
    address=models.CharField(max_length=100,blank=False,null=True)
    contact=models.IntegerField(blank=False,null=True)
    date = models.DateField(null=True,blank=False)
