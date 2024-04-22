from django.urls import path
from auths.views import BloggerCreateUpdateView

urlpatterns = [
    path('register-blogger/', BloggerCreateUpdateView.as_view()),
]
