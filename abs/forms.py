from django.forms import ModelForm
from .models import Post


class PostForms(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'type', 'type_of_housing', 'price', 'number_of_rooms', 'body')
        labels = {
            'title': 'Название',
            'type': 'Тип объявления',
            'type_of_housing': 'Тип квартиры',
            'price': 'Цена',
            'number_of_rooms': 'Количество комнат',
            'body': 'Описание',
        }
