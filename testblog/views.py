from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Post
from .forms import PostForm
from django.forms.models import model_to_dict


def posts(request):
    articles  = Post.objects.all()
    form = PostForm()

    if request.method == "POST":
        if (auth.get_user(request).username):
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.username = auth.get_user(request).username
                post.save()
        else:
            return redirect('/auth/login')

    return render(request, 'posts.html', {'articles': articles, 'form':form })


def delete_post(request, post_id):

    article = Post.objects.get(id=post_id)
    if (auth.get_user(request).username==article.username):
        article.delete()
        return redirect('/posts')
    else:
        return redirect('/auth/login')
