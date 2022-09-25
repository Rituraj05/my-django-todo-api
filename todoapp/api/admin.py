from django.contrib import admin
from .model.models import Task

# Register your models here.
# register Task model with admin so we can perform some basic operations. 
admin.site.register(Task)              