from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, RecommendedPostsView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<str:slug>/', PostDetailView.as_view(), name='post'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<str:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<str:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('recommended/', RecommendedPostsView.as_view(), name='posts_rec'),
]