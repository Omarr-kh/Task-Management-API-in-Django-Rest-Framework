from django.urls import path
from . import views

urlpatterns = [
    path("tasks-list", views.tasks_list, name="tasks-list"),
    path("create-task", views.create_task, name="create-task"),
]
