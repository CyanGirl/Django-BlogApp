from django.shortcuts import render
from .models import Posts, Comments
from .forms import CommentForm, PostForm
from .models import Posts,Comments,Category


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
