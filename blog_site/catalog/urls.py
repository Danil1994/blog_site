from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^posts/$', views.PostListView.as_view(), name='posts'),
    re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post-detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^post/(?P<pk>\d+)/comment_create/$', views.CommentCreate.as_view(), name='comment_create'),
]