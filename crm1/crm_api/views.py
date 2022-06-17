from concurrent.futures.process import _python_exit
from unicodedata import name
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from accounts.models import Customer, Order, Product
from .serializers import cust_serializer,product_serializer,order_serializer
from crm_api import serializers

#=============== CUSTOMER API VIEW ===============
class cust_api_view(APIView):
    permission_classes = [permissions.IsAuthenticated]

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

class cust_detail_api_view(APIView):
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

#=============== PRODUCT API VIEW ===============
class prod_api_view(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = product_serializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        '''
        {
            "name": "",
            "price": "",
            "category": "",
            "description": "",
            "tags": "["",""]",
        }
        '''

        data = {
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'category': request.data.get('category'),
            'description': request.data.get('description'),
            'tags': request.data.get('tags')
        }
        serializer = product_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class prod_detail_api_view(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return None
    
    def get(self, request, pk, *args, **kwargs):
        
        product_instance = self.get_object(pk)
        if not product_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = product_serializer(product_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, *args, **kwargs):
        '''
        Updates the todo item with given pk if exists
        '''
        product_instance = self.get_object(pk)
        if not product_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'category': request.data.get('category'),
            'description': request.data.get('description'),
            'tags': request.data.get('tags')
        }
        serializer = product_serializer(instance = product_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, pk, *args, **kwargs):
        '''
        Deletes the todo item with given pk if exists
        '''
        product_instance = self.get_object(pk)
        if not product_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        product_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


#=============== ORDERS API VIEW ===============
class order_api_view(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = order_serializer(orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        '''
        {
            "customer": ,
            "product": ,
            "status": "",
            "note": ""
        }
        '''

        data = {
            'customer': request.data.get('customer'),
            'product': request.data.get('product'),
            'status': request.data.get('status'),
            'note': request.data.get('note')
        }
        serializer = order_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class order_detail_api_view(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,pk):
        try:
            return Order.objects.get(id=pk)
        except Order.DoesNotExist:
            return None
    
    def get(self, request, pk, *args, **kwargs):
        
        order_instance = self.get_object(pk)
        if not order_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = order_serializer(order_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, *args, **kwargs):
        '''
        Updates the todo item with given pk if exists
        '''
        order_instance = self.get_object(pk)
        if not order_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'customer': request.data.get('customer'),
            'product': request.data.get('product'),
            'status': request.data.get('status'),
            'note': request.data.get('note')
        }
        serializer = order_serializer(instance = order_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, pk, *args, **kwargs):
        '''
        Deletes the todo item with given pk if exists
        '''
        order_instance = self.get_object(pk)
        if not order_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        order_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
