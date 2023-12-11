from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<str:slug>/', PostDetailView.as_view(), name='post'),
    path('create/', PostCreateView.as_view(), name='post_create')
]