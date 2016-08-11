from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .forms import UserForm


def login(request):

    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/posts/cabinet')
        else:
            args['error'] = "User not found"
            return render(request,'login.html',args)
    else:
        return render(request,'login.html',args)


def logout(request):

    auth.logout(request)
    return redirect("/posts")


def register(request):

    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user = auth.authenticate(username=user_form.cleaned_data['username'], password2=user_form.cleaned_data['password2'])
            return redirect('/auth/login')
        else:
            args['form']=user_form
    return render(request,'register.html',args)


@login_required (login_url="/auth/login/")
def edit_profile(request):

    user = request.user
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/posts/cabinet')
    return render(request, 'edit_profile.html', {'user': user, 'form':form })
