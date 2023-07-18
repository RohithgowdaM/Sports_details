from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

# Create your views here.
def test(request):
    while(1):
        return render(request,"home.html")

