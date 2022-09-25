from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100 , blank=True , null=True)
    description = models.TextField(max_length=300, blank=True, null= True) 
    status = models.BooleanField(default=False, blank=True,null=True)
    schedule = models.DateTimeField(auto_now_add=False, auto_now=False,null=True,blank=True)
    created_at= models.DateTimeField(auto_now_add=True, auto_now=False, blank=True,  null=True)
    modified_at= models.DateTimeField(auto_now_add=False, auto_now=True, blank=True,  null=True)
    objects = models.Manager()
    def __str__(self):
        return self.name
