from ..models import Tasks
from django.shortcuts import render


def tasksLog(request):
    try:
        tasks = Tasks.objects.filter(
            user=request.user, datecompleted__isnull=True)
        return render(request, 'tasks.html',
                      {
                          'tasks': tasks

                      })
    except:
        return render(request, 'home.html',
                      {
                          'error': 'no hay logeo de usuario'
                      })
