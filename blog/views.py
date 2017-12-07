# -*- coding=utf8 -*-
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListCreateAPIView

from .models import Record, Comment

from .serializers import CommentSerializer

class CommentView(ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Comment.objects.filter(record_id=pk)
        return queryset

    def perform_create(self, serializer):
        serializer.save(record_id=self.kwargs['pk'])



class RecordListView(ListView):
    model = Record
    context_object_name = 'records'

class RecordDetailView(DetailView):
    model = Record
    context_object_name = 'record'