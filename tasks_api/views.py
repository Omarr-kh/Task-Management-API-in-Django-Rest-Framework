from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@api_view(["GET"])
def tasks_list(request):
    """
    Retrieves all tasks and returns them as a serialized response.
    """
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def view_task(request, pk):
    """
    Retrieves a single task by its ID (`pk`) and returns it as a serialized response.
    """
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def create_task(request):
    """
    Creates a new task with the data provided in the request.
    If the data is valid, the task is saved and returned as a response.
    """
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def update_task(request, pk):
    """
    Updates an existing task by its ID (`pk`).
    - If the task does not exist, a 404 error is returned.
    - The `partial=True` argument allows partial updates, meaning that
      not all fields need to be provided.
    - If the data is valid, the task is updated and returned as a response.
    - If the data is invalid, the errors are returned with a 400 status.
    """
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

    serializer = TaskSerializer(instance=task, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)


@api_view(["DELETE"])
def delete_task(request, pk):
    """
    Deletes a task by its ID (`pk`).
    Returns a confirmation message upon successful deletion.
    """
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Item successfully deleted!")
