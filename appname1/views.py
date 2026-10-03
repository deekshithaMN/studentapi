from django.shortcuts import render
from .serializer import StudentSerializer
from django.http import JsonResponse
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def getDetails(request):
	if request.method=='GET':
		st_data = Student.objects.all()
		serialized_data = StudentSerializer(st_data,many=True)
		return JsonResponse({'details':serialized_data.data})

	if request.method == 'POST':
		serialized_data=StudentSerializer(data=request.data)
		if serialized_data.is_valid():
			serialized_data.save()
			return Response(serialized_data.data,status=status.HTTP_201_CREATED)
		else:
			return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)

    		     
@api_view(['GET','DELETE','PUT'])
def getData(request,id):
	try:
		st_data=Student.objects.get(pk=id)
	except Student.DoesNotExist:
		return Response(status=status.HTTP_400_BAD_REQUEST)
	if request.method=='GET':       
		serialized_data=StudentSerializer(st_data)
		return Response(serialized_data.data)

	if request.method=='DELETE':
		st_data.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	if request.method == 'PUT':
		serialized_data = StudentSerializer(st_data, data=request.data)

	if serialized_data.is_valid():
		serialized_data.save()
		return Response(serialized_data.data, status=status.HTTP_200_OK)
	else:
		return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)






    