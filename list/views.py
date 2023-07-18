from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

# Create your views here.
def list(request):
    return HttpResponse("Hello world")

def homepage(request):  
  return render(request,'homepage.html')

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,'homepage.html')
    return render(request,'homepage.html')
  
def logoutUser(request):
  logout(request)
  return redirect("/homepage")

def student(request):
    return render(request,'student.html')