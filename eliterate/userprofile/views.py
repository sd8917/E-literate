from django.views.generic import TemplateView, ListView

from .models import UserDetail

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = UserDetail
    template_name = 'home.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = UserDetail.objects.filter(
            certificatenumber__exact=query
        )
        print(object_list)
        return object_list