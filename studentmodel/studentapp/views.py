from django.shortcuts import render
from .models import student

def stuFun(request):
    stdata=student.objects.all()
    return render(request,"request.html",{'stlist':stdata})
