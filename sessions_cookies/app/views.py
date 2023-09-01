from django.shortcuts import render
from django.http import HttpResponse

def set_session(request):
    request.session['username'] = 'Meghanath'
    request.session['class']='CSE-3'
    return HttpResponse('Session variable set')

def get_session(request):
    username = request.session.get('username')
    c=request.session.get('class')
    return HttpResponse(f'Username: {username} <br> Class:{c}')

def set_cookie(request):
    response = HttpResponse('Cookie set')
    response.set_cookie('cookie', 'I am a cookie')
    return response

def get_cookie(request):
    cookie = request.COOKIES.get('cookie')
    return HttpResponse(f'Cookie: {cookie}')
