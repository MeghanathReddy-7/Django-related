from django.contrib import admin
from .models import student

class studentview(admin.ModelAdmin):
    list_display=["roll","name","marks"]
admin.site.register(student,studentview)
# Register your models here.
