from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

"""
API Overview
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List View' : '/task-list/v1',
        'Detail View' : '/task-detail/v1/:task_id',
        'Create Task' : '/task-create/v1',
        'Update Task' : '/task-update/v1/:task_id',
        'Delete Task' : '/task-delete/v1/:task_id',
    }
    return Response(api_urls)