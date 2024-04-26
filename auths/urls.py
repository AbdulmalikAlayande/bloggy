from django.urls import path
from auths.views import BloggerCreateUpdateView
from django.urls import include

urlpatterns = [
    path('register-blogger/', BloggerCreateUpdateView.as_view()),
    path('token/', include('auths.token.urls'))
]
