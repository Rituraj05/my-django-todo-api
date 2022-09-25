import imp
from django.urls import path, include 
from .v1 import apiRoutes 
from .v1 import getTaskList 
from .v1 import createTask 
from .v1 import getTaskListById
from .v1 import updateTaskById
from .v1 import deleteTaskById




urlpatterns = [
    path('', apiRoutes.apiOverview, name="api-overview"),
    path('task-list/v1', getTaskList.taskList, name="task-list"),
    path('task-detail/v1/<str:task_id>', getTaskListById.taskDetail, name="task-Detail"),
    path('task-update/v1/<str:task_id>', updateTaskById.taskUpdate, name="task-update"),
    path('task-create/v1', createTask.taskCreate, name="task-Create"),
    path('task-delete/v1/<str:task_id>', deleteTaskById.taskDelete, name="task-delete"),
  ]