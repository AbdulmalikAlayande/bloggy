from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin

from blog.querysets import ALL_POSTS_QUERYSET
from blog.serializers import PostSerializer, BloggerPostsListSerializer
from blog.filters import PostFilter
# Create your views here.

    
class PostAPIView(GenericAPIView):
    queryset = ALL_POSTS_QUERYSET
    serializer_class = PostSerializer
    filter_class = PostFilter
    search_fields = ["title", "blogger__username", "blogger__email", "id", "uuid", "created_at"]
    ordering_fields = ["title", "created_at"]
    ordering = ["-created_at"]

class BloggerPostsListView(ListModelMixin, PostAPIView):
    serializer_class = BloggerPostsListSerializer
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class BloggerPostRetrieveView(RetrieveModelMixin, PostAPIView):

    serializer_class = BloggerPostsListSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class PostListCreateView(CreateModelMixin, PostAPIView):
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
