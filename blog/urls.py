
from django.urls import path
from blog.views import (
    BloggerPostsListView, BloggerPostRetrieveView, PostListCreateView
)

urlpatterns = [
    path('blogger/posts', BloggerPostsListView.as_view()),
    path('blogger/post/<uuid:post_id>', BloggerPostRetrieveView.as_view(lookup_field='uuid')),
    path('post/create-new', PostListCreateView.as_view()),
    # path('post/<post-id>/add-comment', ''),
    # path('post/<post-id>/add-like', ''),
]