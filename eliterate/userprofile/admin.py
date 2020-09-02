from django.contrib import admin
from .models import UserDetail
# Register your models here.

class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('name','phone','certificatenumber')
    list_per_page = 10 #Number of page for display 
    search_fields = ('certificatenumber',)

admin.site.register(UserDetail,UserDetailAdmin)