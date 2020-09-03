from django.shortcuts import render
from django.http import HttpResponse
from .models import UserDetail

def userpage(request):
    getuser = UserDetail.objects.all() #contain all detail about the user
    print(getuser)
    return render(request, 'home.html',{'getuser': getuser})

def search(request):
    pass