from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= '__all__'

# Create your views here.
@api_view(['GET'])
def prodoct(req):
    return Response (ProductSerializer(Product.objects.all(), many=True).data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def members(req):
    return Response ({"access":"success"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register(req):
    User.objects.creat_user()
    return Response ({"access":"success"})
