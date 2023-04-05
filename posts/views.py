from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from posts.models import Post
from posts.forms import PostCreateForm
from django.urls import reverse_lazy


# Create your views here.
class IndexPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class UserPostView(ListView):
    template_name = "user_posts.html"
    model = Post

    def get_queryset(self):
        posts = Post.objects.filter(is_archive=False, author=self.request.user)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PostCreateForm()
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy("my_posts")

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)
