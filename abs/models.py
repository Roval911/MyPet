from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from modules.services.utils import unique_slugify



def upload_path_autor(instance, filename):
    return 'media/posts_images/{0}/{1}'.format(instance.author, filename)

class Post(models.Model):
    class Status(models.TextChoices):
        RENT = 'RT', 'Аренда'
        SALE = 'SL', 'Продажа'

    class TypeOfHousing(models.TextChoices):
        HOUSE = 'HS', 'Дом'
        FLAT = 'FL', 'Квартира'
        ROOM = 'RM', 'Комната'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    type = models.CharField(max_length=2, choices=Status.choices, default=Status.SALE)
    create = models.DateTimeField(auto_now_add=True, )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='abs_post', default=1)
    type_of_housing = models.CharField(max_length=2, choices=TypeOfHousing.choices, default=TypeOfHousing.FLAT)
    price = models.PositiveIntegerField(default=0,)
    number_of_rooms = models.PositiveIntegerField(default=1,)
    views = models.ManyToManyField(User, related_name='post_views', blank=True)
    image = models.ImageField(upload_to=upload_path_autor, blank=True)

    def add_view(self, user):
        if user not in self.views.all():
            self.views.add(user)

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




class PostsImages(models.Model):
    images = models.ImageField(upload_to=upload_path_autor, blank=True)
    post = models.ForeignKey(Post, related_name='PostsImages', on_delete=models.CASCADE)