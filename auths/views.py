from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView
from auths.serializers import CreateBloggerSerializer
from auths.filters import BloggerFilter
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class BloggerAPIView(GenericAPIView):
    # queryset = ALL_BLOGGERS_QUERYSET
    serializer_class = CreateBloggerSerializer
    filter_class = BloggerFilter

    search_fields = ["username", "email", "id", "uuid", "created_at"]
    ordering_fields = ["username", "created_at"]
    ordering = ["-created_at"]

class BloggerCreateUpdateView(CreateModelMixin, UpdateModelMixin, BloggerAPIView):

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
