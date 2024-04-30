from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    Serializer,
    CharField,
    RelatedField,
)
from rest_framework import serializers
from blog.models import Post, Blogger, Comment, Like, Media


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = ["cloud_url"]
        read_only_fields = ["id", "uuid", "created_at"]


class CommentSerializer(ModelSerializer):
    author_username = serializers.CharField(source="author.username", required=True)

    class Meta:
        model = Comment
        fields = ["author_username", "body", "created_at"]
        read_only_fields = ["id", "uuid", "created_at", "is_deleted"]
        extra_kwargs = {
            "created_at": {
                "required": False
            }
        }


class LikeSerializer(ModelSerializer):
    creator_username = CharField(source="creator.username")

    class Meta:
        model = Like
        fields = ["creator_username", "created_at"]
        read_only_fields = ["id", "uuid", "created_at"]


class PostSerializer(ModelSerializer):
    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)
    medias = MediaSerializer(many=True)
    blogger_username = CharField(source="blogger.username")

    class Meta:
        model = Post
        fields = ["blogger_username", "status", "number_of_likes", "title", "body", "likes", "comments", "medias"]
        read_only_fields = ["id", "uuid", "created_at", "blogger", "last_updated"]


class BloggerPostsListSerializer(ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = Post
        fields = ["posts"]


class UrlListingField(RelatedField):

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class PostCreateSerializer(Serializer):
    blogger_email = EmailField(required=True)
    title = CharField(required=True)
    body = CharField(required=True)
    media_urls = UrlListingField(many=True, queryset=Media.objects.all(), required=True)
