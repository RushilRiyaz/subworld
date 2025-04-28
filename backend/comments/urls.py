from django.urls import path
from .views import add_comment

app_name = 'comments'

urlpatterns = [
    path('add/<int:post_id>/', add_comment, name='add_comment'),
]

from .views import add_comment, delete_comment

urlpatterns = [
    path('add/<int:post_id>/', add_comment, name='add_comment'),
    path('delete/<int:comment_id>/', delete_comment, name='delete_comment'),
]