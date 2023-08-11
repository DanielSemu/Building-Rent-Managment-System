from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
#User model
class Role(models.Model):
    Role_name=models.CharField(max_length=100)
    def __str__(self):
        return self.Role_name

class User(AbstractUser):
    Role=models.ForeignKey(Role,on_delete=models.CASCADE,null=True,blank=True)
# class UserAccount(AbstractUser):
#       First_name=models.CharField(max_length=100)
#       Last_name=models.CharField(max_length=100)
#       Role=models.ForeignKey(Role,on_delete=models.CASCADE,null=True,blank=True)
#       username=models.CharField(max_length=200,null=True,unique=True)
#       password=models.CharField(max_length=500)
      
class Block_Location(models.Model):
    Block_Location=models.CharField(max_length=200)
    def __str__(self):
        return self.Block_Location
    
class Block(models.Model):
    Block_name=models.CharField(max_length=200)
    Block_Location=models.ForeignKey(Block_Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.Block_name

class Room(models.Model):
    Room_name=models.CharField(max_length=200)
    Block=models.ForeignKey(Block,on_delete=models.CASCADE)
    Floor=models.CharField(max_length=200)
    Area=models.CharField(max_length=100)
    Price=models.CharField(max_length=100)
    def __str__(self):
        return self.Room_name
    
# Rent Model
# class Rent(models.Model):
#     Client_First_name=models.CharField(max_length=200)
#     Client_Last_name=models.CharField(max_length=200)
#     Start_Day=models.DateField(auto_now=True)
#     End_date=models.DateField()
#     Payed_amount=models.CharField(max_length=100)
#     Total