from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Post, Group
from .forms import CreatePost
from django.contrib.auth.decorators import login_required
from django import views
from django.contrib.auth import get_user_model


def index(request) -> HttpResponse:
    posts = Post.objects.order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    context: dict = {
        'title': 'Последние обновления на сайте',
        'page_obj': page_obj
    }
    return render(request, template_name='posts/index.html', context=context)


def post_detail(request, post_id):
    post = get_object_or_404(klass=Post, pk=post_id)
    if post:
        counter = Post.objects.filter(author=post.author).count()
    context = {
        'post': post,
        'counter': counter
    }
    return render(request, 'posts/post_detail.html', context)


def profile_view(request, username):
    User = get_user_model()
    author = get_object_or_404(klass=User, username=username)
    if author:
        posts = Post.objects.filter(author=author).order_by('-pub_date')
        counter = posts.count()
        paginator = Paginator(posts, 10)
        page = request.GET.get('page', 1)
        page_obj = paginator.get_page(page)
        context = {
            'page_obj': page_obj,
            'author': author,
            'counter': counter
        }
        return render(request,'posts/profile.html', context)



def group_posts(request, slug) -> HttpResponse:
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    context: dict = {
        'title': 'Main page',
        'page_obj': page_obj,
        'group': group
    }
    return render(request=request, template_name='posts/group_list.html', context=context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = CreatePost()
    context = {
        'form': form
    }
    return render(request, 'posts/post.html', context)


class DeletePostView(views.View):
    

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        post.delete()
        return redirect(request.META.get('HTTP_REFERER', 'posts:index'))