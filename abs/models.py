from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from modules.services.utils import unique_slugify


class Post(models.Model):
    class Status(models.TextChoices):
        RENT = 'RT', 'Rent'
        SALE = 'SL', 'Sale'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    type = models.CharField(max_length=2, choices=Status.choices, default=Status.SALE)
    create = models.DateTimeField(auto_now_add=True, )
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='abs_post')

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)
