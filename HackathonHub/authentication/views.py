from django.shortcuts import render ,redirect
from django.http import HttpResponse , JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def Signin(request):
    if request.method=='POST' :
        uname=request.POST['username']
        pword=request.POST['password']

        user=authenticate(username=uname,password=pword)
        person=User.objects.get()


        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("error")
    return render(request, "auth/login.html")

@login_required
def signout(request):
    logout(request)
    return redirect("/")


def signup(request):
        if request.method=='POST' :
            uname=request.POST['username']
            pword=request.POST['password']
            emailid=request.POST["email"]
            myuser = User.objects.create_user(username=uname, email=emailid, password=pword)
            return render(request , "auth/login.html", {"message":"account succefully created , login now"})
        return render(request,"auth/register.html" )
    

