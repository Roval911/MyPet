from django.db.models import Count, Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from .forms import PostForms
from .mixins import AuthorRequiredMixin
from rest_framework import generics, permissions, viewsets

from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'abs/posts.html'
    ordering = ['-create']
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.all()

        if query:
            object_list = object_list.filter(Q(title__icontains=query) | Q(body__icontains=query))

        return object_list

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
        if self.request.user.is_authenticated:
            self.object.add_view(self.request.user)
        context['views_count'] = self.object.views.count()
        return context


class RecommendedPostsView(ListView):
    model = Post
    context_object_name = 'posts_rec'
    template_name = 'abs/recommended_posts.html'
    ordering = ['-views__count']  # Сортировка по количеству просмотров

    def get_queryset(self):
        # Выбираем рекомендуемые статьи, сортируем по количеству просмотров и ограничиваем до 5
        return Post.objects.annotate(views_count=Count('views')).order_by('-views_count')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForms
    template_name = 'abs/create.html'
    login_url = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = 'Создать объявление'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class PostUpdateView(AuthorRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    context_object_name = 'post'
    form_class = PostForms
    template_name = 'abs/update.html'
    login_url = 'posts'
    success_message = 'Успешно обновлено'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактор объявления: {self.object.title}'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PostDeleteView(AuthorRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    template_name = 'abs/delete.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление объявления: {self.object.title}'
        return context


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
