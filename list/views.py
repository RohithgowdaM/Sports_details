from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def test(request):
    while(1):
        return render(request,"home.html")
    
@csrf_exempt
def logi(request):
    if(request.method=="POST"):
        name=request.POST.get("Name")
        password=request.POST.get("password")
        user = authenticate(request,username=name, password=password)
        if user is not None:
            login(request,user)
            return render(request,"sports_det.html")
        else:
            return render(request,"home.html")
    
    
def logout_view(request):
    logout(request)
    return render(request,"home.html")


# if not request.user.is_authenticated: