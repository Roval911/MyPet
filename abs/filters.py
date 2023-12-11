from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = ('type', 'type_of_housing', 'price', 'number_of_rooms')