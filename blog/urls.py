from django.urls import path
from blog.views import (
    BloggerPostsListView,
    BloggerPostRetrieveView,
    PostCreateView,
    PostsListView,
    PostRetrieveView,
    AddCommentView,
    AddLikeView
)

urlpatterns = [
    path("post/create-new", PostCreateView.as_view()),
    path('post/<uuid:pid>/add-comment', AddCommentView.as_view()),
    path('post/<uuid:pid>/add-like', AddLikeView.as_view()),
    path("blogger/<uuid:bid>/posts/", BloggerPostsListView.as_view()),
    path("blogger/<uuid:bid>/post/<uuid:pid>/", BloggerPostRetrieveView.as_view()),
    path("post/<uuid:pid>/", PostRetrieveView.as_view()),
    path("posts/all/", PostsListView.as_view()),
]
