from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Post
from . forms import MakePost,CustionUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    post=Post.objects.all()
    context = {
        "post1":post,
    }
    return render(request,"index.html",context)

def post(request,id):
    post=Post.objects.get(id=id)
    context={
        "post":post
    }
    return render(request,"post.html",context)
@login_required
def make(request):
    form=MakePost()
    context={
        "form":form
    }
    if request.method=='POST':
        form=MakePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"make.html", context)
def edit(request,id):
    post=Post.objects.get(id=id)
    form=MakePost(instance=post)
    context={
        "form":form
    }
    if request.method=='POST':
        form=MakePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"edit.html",context)
def delete(request,id):
    post=Post.objects.get(id=id)    
    if request.method=='POST':
        post.delete()
        return redirect("/")
def logout(request):
    logout(request)
    return redirect('/login')
def signup(request):
    form=CustionUserCreationForm()
    context={
        "form":form
    }
    if request.method=='POST':
        form=CustionUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/login')
    return render(request,"signup.html",context)
