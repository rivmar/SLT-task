from django.conf.urls import url
from .views import RecordListView, RecordDetailView, CommentView

urlpatterns = [
    url(r'^$', RecordListView.as_view(), name='records'),
    url(r'^(?P<pk>[0-9]+)/$', RecordDetailView.as_view(), name='record'),
    url(r'^(?P<pk>[0-9]+)/comments/$', CommentView.as_view(), name='comments')
]
