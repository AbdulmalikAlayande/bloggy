from rest_framework.serializers import ModelSerializer, Serializer
from auths.models import Blogger


class CreateBloggerSerializer(ModelSerializer):

    class Meta:
        model = Blogger
        fields = ["first_name", "last_name", "email", "password", "username", "profile_image_url"]
        read_only_fields = ["id", "uuid", "created_at", "last_updated"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

