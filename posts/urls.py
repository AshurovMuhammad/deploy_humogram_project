from django.urls import path
from posts.views import IndexPage, UserPostView, PostCreateView


urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
    path("my_posts/", UserPostView.as_view(), name='my_posts'),
    path("create_post/", PostCreateView.as_view(), name="create_post")
]