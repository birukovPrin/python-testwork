from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Post
from .models import Comments
from .forms import PostForm
from .forms import CommentForm
from django.forms.models import model_to_dict
from django.template import RequestContext, loader
from django.http import HttpResponse

def posts(request):

    articles  = Post.objects.all()
    return render(request, 'posts.html', {'articles': articles})


def article(request, article_id):

    article = Post.objects.get(id=article_id)
    comments = Comments.objects.filter(article__id = article_id)
    form = CommentForm()
    if request.method == "POST":
        if request.user.is_authenticated() and request.user.username != article.username:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.article = article
                comment.username = request.user.username
                comment.save()
        else:
            return redirect('/auth/login')
    return render(request, 'article.html', {'article': article, 'comments': comments, 'form':form })


@login_required (login_url="/auth/login/")
def profile(request):

    articles = Post.objects.filter(username=request.user.username)
    return render(request, 'cabinet.html', {'articles': articles})


@login_required (login_url="/auth/login/")
def add(request):

    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.username = request.user.username
            post.save()
            return redirect('/posts/cabinet')
    return render(request, 'edit.html', {'form':form })


@login_required (login_url="/auth/login/")
def edit(request, article_id):

    article = Post.objects.get(id=article_id)
    form = PostForm(instance=article)
    if request.user.username==article.username:
        if request.method == "POST":
            form = PostForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('/posts/cabinet')
    else:
        return redirect('/auth/login')
    return render(request, 'edit.html', {'article': article, 'form':form})


@login_required (login_url="/auth/login/")
def delete_post(request, article_id):

    article = Post.objects.get(id=article_id)
    if request.user.username==article.username:
        article.delete()
        return redirect('/posts/cabinet')
    else:
        return redirect('/auth/login')
