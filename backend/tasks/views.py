from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from tasks.serializers import StatusSerializer, TaskSmallSerializer, TaskSerializer, CategorySerializer
from tasks.models import *

class GetListAllTask(generics.ListAPIView):
    """список всех задач"""
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()


class CreateTaskViews(APIView):
    """cоздает задачу"""
    def post(self, request):
        serializer = TaskSmallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetTaskByUser(generics.ListAPIView):
    """получить все задачи конкретного пользователя"""
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_pk = self.kwargs['user_pk']
        return Task.objects.filter(user_id=user_pk).order_by('-id')



class CreateStatusViews(APIView):
    """coздает статус"""
    def post(self,request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateCategoryViews(APIView):
    """cоздает категорию"""
    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)