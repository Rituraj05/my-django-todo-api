from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import TaskSerializer
from ..model.models import Task

"""
Updates the tasks on the basis of task id.
@param id:task_id       
"""
@api_view(['PUT'])
def taskUpdate(request, task_id):
    try:        
         task = Task.objects.get(id = task_id)
         serializer = TaskSerializer(instance=task, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response({
                  "status": "success",
                  "message":"Task Updated Successfully",		
	              "data":serializer.data  
               })
    except:
        return Response({
                "status":"failure"
            })