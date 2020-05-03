from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from instagram.models import Post

class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    model = Post
    template_name = 'index.html'

class PostsDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = '__all__'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy("posts") # cannot use reverse("post") because you cannot jump to the success url while deleting a post