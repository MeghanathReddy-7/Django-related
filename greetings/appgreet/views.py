from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
def greet(request):
    now=datetime.now()
    hour=int(now.strftime("%H"))
    if hour<=12:
        greet="Good Morning"
    elif hour>12 and hour<=16:
        greet="Good Afternoon"
    elif hour>16 and hour<=20:
        greet="Good Evening"
    else:
        greet="Good Night"
    return render(request,'index.html',{"time":now.strftime(" %X"),"greet":greet})