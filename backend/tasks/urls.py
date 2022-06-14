from django.contrib import admin
from django.urls import path, include

from tasks.views import *

urlpatterns = [
    path('list/all/tasks/', GetListAllTask.as_view()),
    path('list/task/user/',GetTaskByToken.as_view()),
    path('create/task/', CreateTaskViews.as_view()),
    path('create/status/',CreateStatusViews.as_view()),
    path('create/category/',CreateCategoryViews.as_view()),
]