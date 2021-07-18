from django.shortcuts import render, redirect
from .forms import AuthorForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import Posts, Comments
from django.contrib.auth.models import User
from usermanage.models import Author


def register(request):

    if request.method == "GET":
        formUser = UserCreationForm()
        formAuth = AuthorForm()
        return render(request, "usermanage/register.html", {"formUser": formUser, "formAuth": formAuth})

    else:
        formUser = UserCreationForm(request.POST)
        if formUser.is_valid():
            user = formUser.save()
            print("Saving User", user)

            formAuth = AuthorForm(request.POST, request.FILES)
            if formAuth.is_valid():
                author = formAuth.save(commit=False)
                author.user = user
                author.save()
                print("Author Saved")
                login(request, user)
                return redirect(reverse("all_blogs"))
            else:
                print(formAuth.errors)
        else:
            print(formUser.errors)
        return redirect(reverse("all_blogs"))


@login_required
def deleteAccount(request, pk):
    if request.method == "GET":
        return render(request, "usermanage/delete_account.html")
    else:
        password = request.POST['password']
        print(password)
        check = authenticate(username=request.user.username, password=password)
        print(check)
        if check == None:
            print("Sorry, password did not match")
            return render(request, "usermanage/delete_account.html")
        else:
            logout(request)
            check.delete()
            print("Account Deleted")
            return redirect(reverse("all_blogs"))


@login_required
def accountDetails(request, pk):

    user = User.objects.get(pk=pk)
    author = Author.objects.get(user=user)
    myposts = Posts.objects.filter(author=user.username).order_by('-post_on')
    mycomments = Comments.objects.filter(
        author=user.username).order_by('-post_on')
    print(author)
    context = {"author": author, "posts": myposts, "comments": mycomments}

    return render(request, 'usermanage/account_details.html', context)


@login_required
def editAccount(request, pk):

    user = User.objects.get(pk=pk)
    author = Author.objects.get(user=user)

    if request.method == "GET":
        form = AuthorForm(instance=author)
    else:
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            print("validated")
            form.save()
        else:
            print(form.errors)
        return redirect("usermanage:account_details", pk)

    return render(request, "usermanage/edit_account.html", {"form": form})
