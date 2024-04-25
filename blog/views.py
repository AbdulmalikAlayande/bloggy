from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin

from auths.models import Blogger
from blog.models import Media, Post
from blog.querysets import ALL_POSTS_QUERYSET
from blog.serializers import (
    PostSerializer,
    BloggerPostsListSerializer,
    PostCreateSerializer,
)
from blog.filters import PostFilter
from commons.utils import get_object_or_404


class PostAPIView(GenericAPIView):
    queryset = ALL_POSTS_QUERYSET
    serializer_class = PostSerializer
    filter_class = PostFilter
    search_fields = [
        "title",
        "blogger__username",
        "blogger__email",
        "id",
        "uuid",
        "created_at",
    ]
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


class PostListRetrieveView(ListModelMixin, RetrieveModelMixin, PostAPIView):

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class PostCreateView(CreateModelMixin, PostAPIView):
    serializer_class = PostCreateSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            blogger: Blogger = get_object_or_404(
                Blogger, email=request.data.get("blogger_email")
            )
            data = serializer.validated_data
            data["blogger"] = blogger
            self.perform_create(data=data)
            headers = self.get_success_headers(serializer.data)
            response_data = {
                "message": "Post created successfully",
                **serializer.validated_data,
                "blogger": blogger.username,
            }
            return Response(
                data=response_data, status=status.HTTP_201_CREATED, headers=headers
            )
        except Exception as exception:
            return Response(
                {"error": str(exception)}, status=status.HTTP_400_BAD_REQUEST
            )

    def perform_create(self, data):
        post = Post(
            title=data.get("title"), body=data.get("body"), blogger=data.get("blogger")
        )
        post.status = Post.Status.PUBLISHED
        post.save()
        media_urls = data.get("mediaUrls")
        for url in media_urls:
            media = Media(cloud_url=url, post=post)
            media.save()
        return post
