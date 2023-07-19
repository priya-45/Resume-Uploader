from django.contrib import admin

# Register your models here.
from .models import ResumeModel

@admin.register(ResumeModel)
class Resume(admin.ModelAdmin):
    list_display = ['name', 'dob', 'gender','locality', 'city', 'pin' , 'state', 'mobile_number', 'email', 'job_city', 'profilephoto', 'my_file', ]
    