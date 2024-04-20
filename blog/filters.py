from django_filters import (
    FilterSet, NumberFilter, CharFilter,
    DateTimeFilter, DateTimeFromToRangeFilter
)
from blog.models import Post, Blogger

class PostFilter(FilterSet):

    blogger = NumberFilter(field_name="blogger")
    date = DateTimeFilter(field_name="created_at")
    date_from_to = DateTimeFromToRangeFilter()
    comment = NumberFilter()

    class Meta:
        model = Post
        fields = ["owner"]

class BloggerFilter(FilterSet):

    email = CharFilter(field_name="email")
    username = CharFilter(field_name="username")

    class Meta:
        model = Blogger
        fields = ["email", "username"]