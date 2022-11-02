from django.shortcuts import render, get_object_or_404, redirect
from ..models import Tasks
from ..forms import TaskForm


def TaskDetailCtrl(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Tasks, pk=task_id,user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'taskDetail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Tasks, pk=task_id,user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'taskDetail.html', {'task': task, 'form': form, 'error': 'error al actualizar'})
