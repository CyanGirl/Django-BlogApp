from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Posts, Comments
from .forms import CommentForm, PostForm
from .models import Posts,Comments,Category
from django.http import HttpResponse
import csv

# for all blogs posted
def all_blogs(request):

    posts = Posts.objects.all().order_by('-post_on')
    if request.method=="POST":

        title,category=request.POST['title'],request.POST['category']
        if len(title)>0:
            posts=Posts.objects.filter(title__icontains=title)
        if len(category)>0:
            if Category.objects.filter(name=category).exists():
                posts=posts.filter(categories=Category.objects.get(name=category))
            else:
                posts=Category.objects.filter(name=category)
        print(posts)
    context = {"posts": posts}

    return render(request, 'app/home.html', context)

def blog_detail(request, pk):

    post = Posts.objects.get(pk=pk)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST,instance=post)
        if form.is_valid():
            author=form.cleaned_data['author']
            description=form.cleaned_data['description']
            comment=Comments(author=author,description=description,post=post)
            comment.save()
            print("saved")
        else:
            print(form.errors)
            print("error")

    comments = Comments.objects.filter(post=post).order_by('-post_on')

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "app/blog_detail.html", context)

def edit_blog(request,pk):

    context={}
    post=Posts.objects.get(pk=pk)
    if request.method=="GET":
        form=PostForm(instance=post)
        return render(request,"app/edit_blog.html",{"form":form,"post":post})
    else:
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            
        else:
            print(form.errors)
        return redirect(reverse("all_blogs"))  

def add_blog(request):

    if request.method=="GET":
        form=PostForm()
        categories=Category.objects.all()
        print(categories)
        context={"form":form,"categories":categories}
        return render(request,"app/add_blog.html",context)

    else:
        form=PostForm(request.POST,request.FILES)
        print(request.POST['categories'])
        print ("Checking",form.is_valid())

        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect(reverse("all_blogs"))

def delete_blog(request,pk):
    print(pk)
    post=get_object_or_404(Posts,pk=pk)
    title=post.title
    if request.method=="GET":
        return render(request,"app/delete_blog.html",{"name":title})
    else:
        blogname=request.POST['blogname']
        print(blogname)
        if blogname==title:
            post.delete()
        else:
            print("Title did not match")
        return redirect(reverse("all_blogs"))

def export_blog(request,pk):

    context={}
    post = Posts.objects.get(pk=pk)
    body=post.body
    title=post.title

    response=HttpResponse(content_type="text/plain")
    response['Content-Disposition']=f'attachment;filename={post.title}.txt'

    writer=csv.writer(response)
    writer.writerow([title])
    writer.writerow([])
    writer.writerow([body])
    return response

