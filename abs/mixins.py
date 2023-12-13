from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.shortcuts import redirect


class AuthorRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        post_author = self.get_object().author
        if request.user == post_author or request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.info(request, 'Изменение и удаление статьи доступно только автору')
            return redirect('posts')
