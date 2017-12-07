# -*- coding=utf8 -*-
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name='Название')

    def __str__(self):
        return self.title

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, verbose_name='Название')
    body = models.TextField(verbose_name='Текст')

    class Meta:
        abstract = True
        ordering = ('-created',)

    def __str__(self):
        return self.title

class Record(BaseModel):
    category = models.ForeignKey(to=Category, null=True, on_delete=models.SET_NULL,verbose_name='Категория')


class Comment(BaseModel):
    record = models.ForeignKey(to=Record, blank=True, on_delete=models.CASCADE, verbose_name='К записи')
    author = models.CharField(max_length=50, blank=True, verbose_name='Автор')

    def __str__(self):
        return self.title, self.author, self.created

