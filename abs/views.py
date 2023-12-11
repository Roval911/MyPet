from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from .forms import PostForms


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'abs/posts.html'
    ordering = ['-create']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'abs/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostForms
    template_name = 'abs/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = 'Создать объявление'
        return context

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForms
    template_name = 'abs/update.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактор объявления: {self.object.title}'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    template_name = 'abs/delete.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление объявления: {self.object.title}'
        return context