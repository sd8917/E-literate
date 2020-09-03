from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

#Write your models here

class UserDetail(models.Model):
    manager            =  models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    name               =  models.CharField(max_length=200, blank=False)
    phone              =  models.BigIntegerField()
    email              =  models.EmailField(max_length=100,unique=True)
    gender             =  models.CharField(max_length=50, choices=(
                             ('male', 'Male'),
                             ('female', 'Female')
                           ))
    profile_picture    =  models.ImageField(upload_to='static/Profile/images',blank=True)
    start_date         =  models.DateTimeField('start-date')
    end_date           =  models.DateTimeField(default=datetime.now) 
    certificatenumber  =  models.CharField(max_length=500) 



    def __str__(self):
        return self.name
