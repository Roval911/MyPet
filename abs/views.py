from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'abs/posts.html'
    ordering = ['-create']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'abs/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context