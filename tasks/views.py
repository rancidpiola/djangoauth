from .controllers.home import homeLog
from .controllers.signin import signinLog
from .controllers.tasks import tasksLog
from .controllers.signup import signupLog
from .controllers.signout import signoutLog
from .controllers.createTask import createTaskCtrl
from .controllers.taskDetail import TaskDetailCtrl
from .controllers.taskCompleteCtrl import task_completeCtrl
from .controllers.taskCompleteCtrl import tasks_completeListCrtl
from .controllers.taskDeleteCtrl import task_Delete
from django.contrib.auth.decorators import login_required



def home(request):
    return homeLog(request)


def signup(request):
    return signupLog(request)

@login_required
def tasks(request):
    return tasksLog(request)

@login_required
def task_Detail(request, task_id):
    return TaskDetailCtrl(request, task_id)

@login_required
def complete_task(request, task_id):
    return task_completeCtrl(request, task_id)

@login_required
def tasks_completedList(request):
    return tasks_completeListCrtl(request)

@login_required
def delete_task(request, task_id):
    return task_Delete(request, task_id)

@login_required
def createTask(request):
    return createTaskCtrl(request)

@login_required
def signout(request):
    return signoutLog(request)


def signin(request):
    return signinLog(request)
