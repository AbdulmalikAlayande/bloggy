from rest_framework.serializers import ModelSerializer

from auths.models import Blogger


class CreateBloggerSerializer(ModelSerializer):

    class Meta:
        model = Blogger
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "username",
            "profile_image_url",
        ]
        read_only_fields = ["id", "uuid", "created_at", "last_updated"]
        extra_kwargs = {
            "password": {"write_only": True, "max_length": 128},
            "first_name": {"max_length": 120},
            "last_name": {"max_length": 120},
            "email": {"max_length": 120},
            "username": {"max_length": 120},
        }
