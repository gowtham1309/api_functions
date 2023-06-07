from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from app1.models import *

from app1.serializers import *
from rest_framework.response import Response
from rest_framework import status

@api_view()
def employeeobject(request):
    EQS=Employee.objects.all()#LOEO
    ESD=EmployeeMS(EQS,many=True)
    return Response(ESD.data)

