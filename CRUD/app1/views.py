from django.shortcuts import render,redirect
from .models import student
from .forms import studentform
from django.http import *
def add(request):
    form=studentform()
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    return render(request,'add.html',{'form':form})
def show(request):
    students=student.objects.all()
    return render(request,'show.html',{'form':students})
def delete(request,id):
    studentob=student.objects.get(id=id)
    studentob.delete()
    return redirect('show')
def update(request,id):
    studentob=student.objects.get(id=id)
    form=studentform(instance=studentob)
    if request.method=='POST':
        form=studentform(request.POST,instance=studentob)
        if form.is_valid():
            form.save()
            return redirect('show')
    return render(request,'update.html',{'form':form})