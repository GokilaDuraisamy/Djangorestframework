from django.db import models



# Create your models here.
class student_details(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True,)
    email= models.EmailField(max_length=255,blank=True, null=True,unique=True,)
    branch = models.CharField(max_length=255,blank=True, null=True,)
    bio = models.TextField(blank=True, null=True,)



    def __str__(self):
        return self.name
