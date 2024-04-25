from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView
from auths.serializers import CreateBloggerSerializer
from auths.filters import BloggerFilter
from rest_framework import status
from rest_framework.response import Response

from auths.utils import send_registration_successful_mail


# Create your views here.

class BloggerAPIView(GenericAPIView):
    # queryset = ALL_BLOGGERS_QUERYSET
    serializer_class = CreateBloggerSerializer
    filter_class = BloggerFilter

    search_fields = ["username", "email", "id", "uuid", "created_at"]
    ordering_fields = ["username", "created_at"]
    ordering = ["-created_at"]

class BloggerCreateUpdateView(CreateModelMixin, UpdateModelMixin, BloggerAPIView):
    template_name = "registration_successful.html"
    EMAIL_SUBJECT = "Registration Was Successful"

    def post(self, request, *args, **kwargs):
        serializer: CreateBloggerSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        send_registration_successful_mail(
            to=[serializer.validated_data.get("email")],
            name=serializer.validated_data.get("first_name"),
            subject=self.EMAIL_SUBJECT,
            template=self.template_name
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
