from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from tasks.serializers import StatusSerializer, TaskSmallSerializer, TaskSerializer, CategorySerializer
from tasks.models import *
from datetime import datetime

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


class GetTaskByToken(generics.ListAPIView):
    """получить задачи по токену"""
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.filter(user_id=self.request.user.id).order_by('-id')
        # получаем просроченый статус
        expired = Status.objects.get(id=3)
        s = ChangeStatus(queryset,expired)
        query_set = s.check()
        return query_set



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


class ChangeStatus():
    "меняет статус задачи если время вышло"
    def __init__(self,queryset,expired):
        self.queryset = queryset
        self.expired = expired

    def check(self):
        today = datetime.now()
        for query in self.queryset:
            if today > query.endtime.replace(tzinfo=None):
                query.status = self.expired
                query.save()
        return self.queryset

