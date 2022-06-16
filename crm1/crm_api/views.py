from concurrent.futures.process import _python_exit
from unicodedata import name
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from accounts.models import Customer
from .serializers import cust_serializer
from crm_api import serializers

# Create your views here.


class crm_api_view(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        serializer = cust_serializer(customers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        '''
        {
            "user": "",
            "name": "",
            "phone": ,
            "email": "",
        }
        '''

        data = {
            'user': request.data.get('user'),
            'name': request.data.get('name'),
            'phone': request.data.get('phone'),
            'email': request.data.get('email')
        }
        serializer = cust_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class crm_detail_api_view(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,pk):
        try:
            return Customer.objects.get(id=pk)
        except Customer.DoesNotExist:
            return None
    
    def get(self, request, pk, *args, **kwargs):
        
        cust_instance = self.get_object(pk)
        if not cust_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = cust_serializer(cust_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, *args, **kwargs):
        '''
        Updates the todo item with given pk if exists
        '''
        cust_instance = self.get_object(pk)
        if not cust_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'user': request.data.get('user'),
            'name': request.data.get('name'),
            'phone': request.data.get('phone'),
            'email': request.data.get('email')
        }
        serializer = cust_serializer(instance = cust_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, pk, *args, **kwargs):
        '''
        Deletes the todo item with given pk if exists
        '''
        cust_instance = self.get_object(pk)
        if not cust_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        cust_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )