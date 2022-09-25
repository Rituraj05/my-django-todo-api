from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import TaskSerializer
from ..model.models import Task

"""
Delete a task on the basis of task id.
@param id:task_id 
"""
@api_view(['DELETE'])
def taskDelete(request, task_id):
    try:
        task = Task.objects.get(id = task_id)
        task.delete()
        return Response({
            "status": "success",
            "message":"Task Deleted successfully"  
	     })
    except:
        return Response({
                "status":"failure"
            })