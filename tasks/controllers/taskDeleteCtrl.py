from django.shortcuts import  get_object_or_404, redirect
from ..models import Tasks


def task_Delete(request,task_id):
    task = get_object_or_404(Tasks,pk=task_id,user=request.user)
    if request.method =='POST':
        task.delete()
        return redirect('tasks')