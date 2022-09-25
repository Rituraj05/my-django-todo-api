from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import TaskSerializer
from ..model.models import Task

"""
Create a new task        
"""
@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        "status": "success",
        "message":"Task Created Successfully",		
	    "data":serializer.data  
	})