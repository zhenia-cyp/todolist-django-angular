import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """модель категории"""
    name = models.CharField('название категории',max_length=200)

    def __str__(self):
        return '{0}'.format(self.name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-id']


class Status(models.Model):
    """модель статуса задачи"""
    name = models.CharField('статус',max_length=200)

    def __str__(self):
        return '{0}'.format(self.name)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Cтатусы'
        ordering = ['-id']


class Task(models.Model):
    """модель задачи task"""
    title = models.CharField('заголовок', max_length=200)
    text = models.TextField('описание задачи')
    starttime = models.DateTimeField('время создания',auto_now=True)
    endtime = models.DateTimeField('время завершения', auto_now=True)
    category = models.ForeignKey(Category,verbose_name='категория задачи',on_delete=models.CASCADE)
    status = models.ForeignKey(Status,verbose_name='текущий статус',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return '{0} {1} {2} {3} {4} {5}'.format(self.title, self.category, self.text, self.starttime, self.endtime, self.status)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

