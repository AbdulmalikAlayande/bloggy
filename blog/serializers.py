from rest_framework.serializers import ModelSerializer, Serializer, CharField

from blog.models import Post, Blogger, Comment, Like, Media


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"
        read_only_fields = ["id", "uuid", "created_at"]

class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        field = "__all__"
        read_only_fields = ["id", "uuid", "created_at"]

class LikeSerializer(ModelSerializer):

    class Meta:
        model = Like
        fields = "__all__"
        read_only_fields = ["id", "uuid", "created_at"]

class PostSerializer(ModelSerializer):
    
    medias = MediaSerializer(many=True, required=False)
    comments = CommentSerializer(many=True, required=False)
    likes = LikeSerializer(many=True, required=False) 

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["id", "uuid", "created_at", "blogger"]


class BloggerSerializer(ModelSerializer):

    class Meta:
        model = Blogger
        fields = "__all__"
        read_only_fields = ["id", "uuid", "created_at"]
        write_only_fields = ["password"]


class BloggerPostsListSerializer(Serializer):
    blogger_username = CharField(max_length=255, required=True)
    posts = PostSerializer(many=True, required=False)

