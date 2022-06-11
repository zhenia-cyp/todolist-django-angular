from rest_framework import serializers
from tasks.models import *


class CategorySerializer(serializers.ModelSerializer):
    """категория"""
    class Meta:
        model = Category
        fields = ['id','name']


class StatusSerializer(serializers.ModelSerializer):
    "статус"
    class Meta:
        model = Status
        fields= ['id','name']


class TaskSerializer(serializers.ModelSerializer):
    "nested task serializer"
    category = CategorySerializer(read_only=True, many=False)
    status = StatusSerializer(read_only=True, many=False)

    class Meta:
        model = Task
        fields = ['id','category','title','text','status','starttime','endtime']


class TaskSmallSerializer(serializers.ModelSerializer):
    "simple task serializer "
    starttime = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    endtime = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model = Task
        fields = ['category','title','text','status','starttime','endtime']