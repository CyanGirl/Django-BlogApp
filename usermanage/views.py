from django.shortcuts import render,redirect
from .forms import AuthorForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    
    if request.method=="GET":
        formUser=UserCreationForm()
        formAuth=AuthorForm()
        return render(request,"usermanage/register.html",{"formUser":formUser,"formAuth":formAuth})

    else:
        formUser=UserCreationForm(request.POST)
        if formUser.is_valid():
            user=formUser.save()
            print("Saving User",user)

            formAuth=AuthorForm(request.POST,request.FILES)
            if formAuth.is_valid():
                author=formAuth.save(commit=False)
                author.user=user
                author.save()
                print("Author Saved")
                login(request,user)
                return redirect(reverse("all_blogs"))
            else:
                print(formAuth.errors)
        else:
            print(formUser.errors)
        return redirect(reverse("all_blogs"))

def deleteAccount(request,pk):
    if request.method=="GET":
        return render(request,"usermanage/delete_account.html")
    else:
        password=request.POST['password']
        print(password)
        check=authenticate(username=request.user.username,password=password)
        print(check)
        if check ==None:
            print("Sorry, password did not match")
            return render(request,"usermanage/delete_account.html")
        else:
            logout(request)
            check.delete()
            print("Account Deleted")
            return redirect(reverse("all_blogs"))
   

