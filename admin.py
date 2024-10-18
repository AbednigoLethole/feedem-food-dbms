from django.contrib import admin
from .models import Student

# Register your models here.
#giving the Admin access to student database
admin.site.register(Student)
