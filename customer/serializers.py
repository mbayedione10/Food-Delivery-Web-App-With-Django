from rest_framework import serializers, generics, permissions, status
from customer.models import *

from rest_framework import serializers
from django.contrib.auth import authenticate

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'