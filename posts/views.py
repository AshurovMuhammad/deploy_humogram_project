from django.shortcuts import render
from django.views.generic import TemplateView
from posts.models import Post


# Create your views here.
class IndexPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class UserPostView(TemplateView):
    template_name = "user_posts.html"

