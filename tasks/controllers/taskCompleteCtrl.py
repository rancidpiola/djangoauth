

from django.shortcuts import get_object_or_404, redirect, render
from ..models import Tasks
from django.utils import timezone


def task_completeCtrl(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')


def tasks_completeListCrtl(request):
        tasks = Tasks.objects.filter(
        user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
        return render(request, 'tasks.html', {'tasks': tasks})
