from dataclasses import field
from rest_framework import serializers
from accounts.models import Customer

class cust_serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["user", "name", "phone", "email", "date_created", "profile_pic"]