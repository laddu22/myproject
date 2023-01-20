from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
#import datetimefrom django.datetime import datetime
import datetime
from django.conf import settings

class CustomUser(AbstractUser):
    UploadPhoto = models.ImageField(upload_to="pics",help_text='Please upload recent color photo')
    DateOfBirth = models.DateField(blank=False,auto_now_add=True)
   # InitialInvestmentAmount = models.BigIntegerField(blank="True",null='False')
    
    def __unicode__(self):
        return self.user.id


# Create your models here.
class Tasklist(models.Model):
    CHOICES = (
        ('Gold', 'Gold'),
        ('Stocks', 'Stocks'),
        ('Bonds', 'Bonds'),
        ('Mutual Funds', 'Mutual Funds'),  
    )
    manage = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)
    task = models.CharField(max_length=150,choices=CHOICES,default='Mutual Funds')
    done = models.BooleanField(default=False)
    amount=models.IntegerField(default=1000,null=True,blank=True)
    Date = models.DateTimeField(default=datetime.datetime.now())


    def __str__(self):
        return (self.task) + '-' + str(self.done)


class request_from_contact(models.Model):
    name= models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    message = models.TextField(max_length=150,null=True)
    
    class meta:
        ordering = ['name','email']

    def __str__(self):
        return (self.name)

class request_call(models.Model):
    MobileNo = models.IntegerField()
    ChooseDate = models.DateField()

    def __str__(self):
        return str(self.MobileNo)




