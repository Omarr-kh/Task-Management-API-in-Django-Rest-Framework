from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def tasks_list(request):
    data = {
        "name": "omar",
        "age": 21,
        "status": "single",
    }
    return Response(data)
