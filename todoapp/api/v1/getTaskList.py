from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import TaskSerializer
from ..model.models import Task

"""
Returns all task lists
"""
@api_view(['GET'])
def taskList(request):  
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)    
        return Response({
        "status": "success",
		"results": len(serializer.data),		
		"data": {"data":serializer.data } 
	    })