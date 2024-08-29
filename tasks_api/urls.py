from django.urls import path
from . import views

urlpatterns = [
    path("tasks-list", views.tasks_list, name="tasks-list"),
    path("create-task", views.create_task, name="create-task"),
    path("view-task/<int:pk>", views.view_task, name="view-task"),
    path("update-task/<int:pk>", views.update_task, name="update-task"),
    path("delete-task/<int:pk>", views.delete_task, name="delete-task"),
]
