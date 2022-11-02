from django.shortcuts import render, redirect
from ..forms import TaskForm


def createTaskCtrl(request):
    if request.method == "GET":
        return render(request, 'create.html', {'form': TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            newTask = form.save(commit=False)
            newTask.user = request.user
            newTask.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create.html',
                          {
                              'form': TaskForm,
                              'error': 'no esta bien la info'
                          })
