from tkinter.tix import Tree
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True


    def create_user(self,email,password=None,**extra_fields):

        if not email:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('role',1)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff true')

        return self.create_user(email,password,**extra_fields)



class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.state_name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=45, unique=True)
    state= models.ForeignKey(State, on_delete=models.PROTECT, related_name='State_Id')
    
    def __str__(self):
        return self.city_name

    class Meta:
         verbose_name = "Citie"

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=14,null=True,blank=True)
    email_token = models.CharField(max_length=100,null=True,blank=True)
    role = models.SmallIntegerField(choices=((1,'Admin'),(2,'Guide'),(3,'Delivery Boy'),(4,'Customer')),default=4)
    address = models.CharField(max_length=200,null=True,blank=True)
    pincode  = models.CharField(max_length=6, validators=[MinValueValidator(100000), MaxValueValidator(999999)],null=True,blank=True)
    city = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    objects = UserManager()
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []

