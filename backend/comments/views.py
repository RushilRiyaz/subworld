from django.shortcuts import redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm
from feed.models import Post
from django.contrib.auth.decorators import login_required

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.id)  
    return redirect('post-detail', pk=post.id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id  

    if request.user == comment.user:
        comment.delete()

    return redirect('post-detail', pk=post_id)