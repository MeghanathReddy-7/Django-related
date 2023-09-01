from django.contrib import admin
from .models import student

class studentlist(admin.ModelAdmin):
    list_display=['Name','id','email']
admin.site.register(student,studentlist)
# Register your models here.
