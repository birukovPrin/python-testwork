from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/posts')
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
