from django.db.models import QuerySet
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin

from auths.models import Blogger
from auths.permissions import IsAuthenticatedUser, IsAdminUser
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
    # permission_classes = [IsAuthenticatedUser]
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

    def get(self, request: Request, *args, **kwargs):
        blogger: Blogger = get_object_or_404(Blogger, uuid=kwargs.get("bid"))
        posts = self.get_queryset().filter(blogger=blogger)
        response_data = [self.get_serializer(post).data for post in posts]
        return Response(data=response_data, status=status.HTTP_200_OK)


class BloggerPostRetrieveView(RetrieveModelMixin, PostAPIView):

    def get(self, request, *args, **kwargs):
        blogger: Blogger = get_object_or_404(Blogger, uuid=kwargs.get("bid"))
        post: Post = (self.get_queryset().filter(blogger=blogger).get(uuid=kwargs.get("pid")))
        serializer: PostSerializer = self.get_serializer(post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


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


"""
response_data = {
            "message": "Post Was Found",
            "post": {
                "blogger_username": post.blogger.username,
                "status": post.status,
                "title": post.title,
                "body": post.body,
                "likes": len(list(post.likes.all())),
                "comments": list(
                    post.comments.all().values("author__username", "body")
                ),
                "medias": list(post.medias.all().values("created_at", "cloud_url")),
            },
        }
"""
