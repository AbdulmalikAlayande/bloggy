from rest_framework.serializers import ModelSerializer

from blog.models import Post


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["id", "uuid", "created_at", "blogger"]
        
