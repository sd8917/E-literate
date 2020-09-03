
from django.urls import path

from .import views

app_name='userprofile'

urlpatterns = [
    path('',views.userpage,name='userpage'),
    path('search/', views.search, name='search'),
]
