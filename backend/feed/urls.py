from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, SearchPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='feed-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('search_posts', SearchPostListView.as_view(), name='search-posts'),
	path('post_like/<int:pk>', views.post_like, name='post_like'),
    path('bookmarks/', views.BookmarkListView.as_view(), name='bookmark_list'),
    path('post/<int:pk>/bookmark/', views.toggle_bookmark, name='toggle_bookmark'),
]