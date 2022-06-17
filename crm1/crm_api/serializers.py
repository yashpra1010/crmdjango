from dataclasses import field
from rest_framework import serializers
from accounts.models import Customer, Order, Product

class cust_serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["user", "name", "phone", "email", "date_created", "profile_pic"]

class product_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "category", "description", "date_created","tags"]

class order_serializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["customer", "product", "date_created", "status", "note"]