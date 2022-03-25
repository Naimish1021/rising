from ast import Try
from enum import unique
from sqlite3 import Timestamp
from statistics import mode
from django.core.exceptions import ValidationError
from django.db import models
from razorpay import Customer
from account.models import *
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator

class Offer(models.Model):
    offer_id = models.AutoField(primary_key=True)
    offer_name = models.CharField(max_length=45, unique=True)
    start_date = models.DateField(default=now)
    end_date = models.DateField(default=now)
    discount = models.FloatField()

    def __str__(self):
        return self.offer_name

class Visit_Place(models.Model):
    place_name = models.CharField(max_length=25,unique=True)
    image = models.ImageField(upload_to = 'package/place')
    address = models.CharField(max_length=70, null=True, blank=True)
    pin_code = models.PositiveSmallIntegerField(null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='c_id')
    
    def clean(self):
        if len(str(self.pin_code)) != 6:
            raise ValidationError("pin code must be 6 digit")

    def __str__(self):
        return self.place_name

    class Meta:
         verbose_name = "Visit Place"

class Package(models.Model):
    name = models.CharField(max_length=100, unique=True)
    caption = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    days = models.PositiveSmallIntegerField(default=1)
    nights = models.PositiveSmallIntegerField()
    max_altitude = models.PositiveSmallIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to = 'package/image', default="")
    eventpageimage = models.ImageField(upload_to = 'package/image', default="")
    offer = models.ManyToManyField(Offer, related_name='of_id',blank=True)
   

    def clean(self):
        if self.days == 0:
            raise ValidationError("Number of days should be grater than 0")
        return super().clean()
    def __str__(self):
        return self.name


class PackageDate(models.Model):
    package = models.ForeignKey(Package,on_delete=models.CASCADE)
    date = models.DateField(default=now)
    guide = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserId',limit_choices_to={'role':2}, null=True, blank=True)
    maxPerson = models.SmallIntegerField(default=0,validators=[MinValueValidator(10), MaxValueValidator(20)])
    def __str__(self):
        return  str(self.package) + ' ' + 'Star from ' + str(self.date.strftime('%d/%m/%Y'))

    def clean(self):
        if now().date() > self.date:
            raise ValidationError("Date is incorrect")

    class Meta:
        unique_together = ("package", "date", )

class JoinFrom(models.Model):
    join_from = models.CharField(max_length=30)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='pck_id')
    amount = models.PositiveIntegerField(null=True, blank=True)
    place = models.ForeignKey(Visit_Place,on_delete=models.CASCADE)
    
    def clean(self) -> None:
        if self.amount == 0:
            raise ValidationError('Amount should be greater than 0')
        return super().clean()
    def __str__(self):
        return  str(self.package) + ' ' + 'Join from ' + self.join_from

    class Meta:
        unique_together = ("package", "place", )
    

class Schedule(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='PackageId')
    dayNo = models.SmallIntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(15)])
    currentPlace = models.ForeignKey(Visit_Place,on_delete=models.CASCADE)
    placeCaption = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, null=True, blank=True)
    class Meta:
        unique_together = ("package", "dayNo", )
    


class Package_Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    package = models.ForeignKey(PackageDate, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'role':4},  null=True, blank=True)
    joinFrom = models.ForeignKey(JoinFrom,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=13)
    booking_date = models.DateField(default=now)
    status = models.SmallIntegerField(choices=((1,'Booked'),(2,'Completed'),(3,'Canceled')),default=1)
    amount = models.PositiveIntegerField(default=0)
    city = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=200)
    pin_code = models.CharField(max_length=6)
    noOfPerson = models.SmallIntegerField(default=1)
    razorpay_booking_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name+" has booked with id"+str(self.booking_id)


    class Meta:
        verbose_name = "Package Booking"
    
class PackageCancel(models.Model):
    booking=models.ForeignKey(Package_Booking,on_delete=models.CASCADE)
    date = models.DateField(default=now)
    reason = models.CharField(max_length=200,null=True,blank=True)   
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.name
    
   

class PackageFeedback(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=100)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    timeStamp =models.DateTimeField(default=now)
    class Meta:
        unique_together = ("customer", "package", )

class Notificaton(models.Model):
    type = models.SmallIntegerField(choices=((1,'package'),(2,'order'),(3,'order cancel'),(4,'return'),(5,'package Cancel')))
    pid = models.IntegerField()
    is_seen = models.BooleanField(default=False)