from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.db.models import Count
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from models.models import Post, PostCategory, CommentPost

# Create your views here.


class PostListView(generic.ListView):
    queryset = Post.objects.filter(active=True)
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_categories'] = PostCategory.objects.annotate(
            count_post=Count('posts')
        ).all()
        return context


class PostDetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self):
        post_obj = get_object_or_404(Post, pk=self.kwargs['pk'])
        return post_obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_categories'] = PostCategory.objects.annotate(
            count_post=Count('posts')
        ).all()
        context['posts'] = Post.objects.filter(active=True)
        return context
    

@login_required
@require_POST
def add_comment_post_view(request, pk):
    post_obj = get_object_or_404(Post, pk=pk)
    CommentPost.objects.create(
        post_id=post_obj.pk,
        user_id=request.user.pk,
        text=request.POST.get('text')
    )
    return redirect(reverse('blog:post_detail', kwargs={'pk': post_obj.pk}))
