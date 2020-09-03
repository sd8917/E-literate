from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserDetail
from django.db.models import Q

def userpage(request):
    getuser = UserDetail.objects.all() #contain all detail about the user
    print(getuser)
    return render(request, 'home.html',{'getuser': getuser})

#this function return the user query into templates
#working on
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
    
        search_results = UserDetail.objects.filter(
           Q(certificatenumber__iexact = search_term) 
        )
        print(str(search_term))
        context = {
            'search_term' : search_term,
            'search_results': search_results.filter(manager=request.user)
        }
        return render(request, 'home.html', context)
        
    else:

        return redirect(request, 'home.html')