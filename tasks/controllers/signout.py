from django.contrib.auth import logout
from django.shortcuts import  redirect

def signoutLog(request):
    logout(request)
    return redirect('home')
