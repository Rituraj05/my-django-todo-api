from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import TaskSerializer
from ..model.models import Task

"""
 Get task details on the basis of task id 
 @param id:task_id
"""
@api_view(['GET'])
def taskDetail(request, task_id):    
    try:
        tasks = Task.objects.get(id=task_id)
        serializer = TaskSerializer(tasks, many = False)
        return Response({
            "status": "success",		
	        "data":serializer.data  
	    })
    except:
        return Response({
                "status":"failure"
            })