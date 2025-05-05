from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q, Count
from comments.forms import CommentForm
from .models import Post
from .filters import SandwichFilter
from .models import Bookmark
from django.contrib.auth.decorators import login_required
from django.urls import reverse


class PostListView(ListView):
    model = Post
    template_name = 'feed/home.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        queryset = Post.objects.all().annotate(
            num_likes=Count('likes')).order_by('-date_posted')
        self.filterset = SandwichFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset

        # CLEAN UP FILTER VALUES
        filters_applied = []
        get_data = self.request.GET

        for key, value in get_data.items():
            if not value or key == 'page':
                continue

            # MULTI SELECT
            if key in ['veggies', 'sauces']:
                values = get_data.getlist(key)
                for v in values:
                    if v == 'None':
                        label = 'No Vegetables' if key == 'veggies' else 'No Sauce'
                        filters_applied.append(label)
                    else:
                        filters_applied.append(v)
            else:

                # REST
                if key == 'meat' and value == 'None':
                    filters_applied.append('No Meat')
                elif key == 'cheese' and value == 'None':
                    filters_applied.append('No Cheese')
                elif key == 'price__gt':
                    filters_applied.append(f"Min: {value}€")
                elif key == 'price__lt':
                    filters_applied.append(f"Max: {value}€")
                elif key == 'sort':
                    filters_applied.append(value.capitalize())
                else:
                    filters_applied.append(value)

        context['filters_applied'] = filters_applied
        return context


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
        queryset = Post.objects.all().order_by('-date_posted')
        query = self.request.GET.get('query')

        if query:
            if query.lower() == 'vegan':
                queryset = Post.objects.filter(
                    vegan__iexact='Vegan').order_by('-date_posted')
            elif query.lower() == 'non vegan':
                queryset = Post.objects.none()
            else:
                queryset = Post.objects.filter(
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
        return queryset


def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    # Redirect based on where the request came from
    return redirect(request.META.get('HTTP_REFERER', 'home'))


class PostDetailView(DetailView):
    model = Post
    template_name = 'feed/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        if self.request.user.is_authenticated:
            context['is_bookmarked'] = Bookmark.objects.filter(user=self.request.user, post=self.object).exists()
        else:
            context['is_bookmarked'] = False
        return context


class BookmarkListView(ListView):
    model = Post
    template_name = 'feed/bookmark_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        bookmarks = Bookmark.objects.filter(user=self.request.user).select_related('post')
        posts = [bookmark.post for bookmark in bookmarks]
        return posts

@login_required
def toggle_bookmark(request, pk):
    post = get_object_or_404(Post, pk=pk)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, post=post)

    if not created:
        bookmark.delete()

    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    else:
        return redirect('post-detail', pk=post.pk)
