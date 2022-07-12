from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from tasks.serializers import StatusSerializer, TaskSmallSerializer, TaskSerializer, CategorySerializer
from tasks.models import *
from datetime import datetime



class ItemTaskViews(APIView):
    """получаем конкретную задачу по id"""
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TaskSerializer(snippet)
        return Response(serializer.data)

    """редактируем текущую задачу"""
    def patch(self, request, pk):
        obj = self.get_object(pk)
        # set partial=True to update a data partially
        serializer = TaskSerializer(obj, data=request.data,partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



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



class GetTasksByToken(generics.ListAPIView):
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

