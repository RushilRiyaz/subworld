from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q


class PostListView(ListView):
    model = Post
    # expects <app>/<model>_<viewtype>.html | feed/post_list.html
    template_name = 'feed/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['sandwich', 'about', 'vegan', 'size', 'bread', 'meat', 'cheese', 'sauce_1', 'sauce_2',
              'sauce_3', 'veggie_1', 'veggie_2', 'veggie_3', 'temp', 'price', 'sandwich_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['sandwich', 'about', 'vegan', 'size', 'bread', 'meat', 'cheese', 'sauce_1', 'sauce_2',
              'sauce_3', 'veggie_1', 'veggie_2', 'veggie_3', 'temp', 'price', 'sandwich_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserPostListView(ListView):
    model = Post
    template_name = 'feed/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class SearchPostListView(ListView):
    model = Post
    template_name = 'feed/search_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('query')
        print("Query:", query)
        if query:
            # Handle Vegan specifically
            if query.lower() == 'vegan':
                return Post.objects.filter(vegan__iexact='Vegan').order_by('-date_posted')
            elif query.lower() == 'non vegan':
                return Post.objects.none()  # Non Vegan is not searchable
            else:
                return Post.objects.filter(
                    Q(sandwich__icontains=query) |
                    Q(about__icontains=query) |
                    Q(bread__icontains=query) |
                    Q(meat__icontains=query) |
                    Q(cheese__icontains=query) |
                    Q(sauce_1__icontains=query) |
                    Q(sauce_2__icontains=query) |
                    Q(sauce_3__icontains=query) |
                    Q(veggie_1__icontains=query) |
                    Q(veggie_2__icontains=query) |
                    Q(veggie_3__icontains=query) |
                    Q(temp__icontains=query) |
                    Q(size__icontains=query)
                ).order_by('-date_posted')
        return Post.objects.none()


def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    # Redirect based on where the request came from
    return redirect(request.META.get('HTTP_REFERER', 'home'))
