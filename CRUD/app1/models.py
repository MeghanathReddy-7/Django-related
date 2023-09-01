from django.db import models

class student(models.Model):
    Name=models.CharField(max_length=20)
    id=models.IntegerField(primary_key=True)
    email=models.EmailField()
# Create your models here.
