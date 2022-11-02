from django.shortcuts import render


def homeLog(request):
    return render(request, 'home.html')

