from django.urls import path
from blog.views import (
    BloggerPostsListView,
    BloggerPostRetrieveView,
    PostCreateView,
    PostListRetrieveView,
)

urlpatterns = [
    path("blogger/<uuid:bid>/posts/", BloggerPostsListView.as_view()),
    path(
        "blogger/<uuid:bid>/post/<uuid:pid>/",
        BloggerPostRetrieveView.as_view(),
    ),
    path("posts/<uuid:pid>/", PostListRetrieveView.as_view()),
    path("post/create-new", PostCreateView.as_view()),
    # path('post/<post-id>/add-comment', ''),
    # path('post/<post-id>/add-like', ''),
]
