from django.db import models

class student(models.Model):
    roll=models.IntegerField()
    name=models.TextField(max_length=20)
    marks=models.IntegerField()