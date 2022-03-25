from pyexpat import model
from tabnanny import verbose
from django.db import models
import razorpay
from account.models import User
from package.models  import Offer
from django.utils.timezone import now
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key = True)
    category_name = models.CharField(max_length = 25, unique=True)
    subcategory = models.ForeignKey('self', on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self): 
        return self.category_name


class Product(models.Model):
    product_id = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quntity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=2000, default="")
    image = models.ImageField(upload_to = 'product/image', default="")
    offer = models.ManyToManyField(Offer,blank=True)
    class Meta:
        unique_together = ('product_name', 'price')

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return 'User: ' + str(self.user_id) + ' Quantity: ' + str(self.quantity) + ' Price: ' +  str(self.price)
    


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(default= now)
    amount = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=30)  
    state = models.CharField(max_length=30)
    pin_code = models.PositiveIntegerField(validators=[MinValueValidator(100000), MaxValueValidator(999999)])
    address = models.CharField(max_length=200)
    customer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='ctmr', null=True, blank=True)
    Delivery_boy = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'role':3}, related_name='delivery_boy', null=True, blank=True)
    STATUS_CHOICES = (
        (1, 'Confirmed'),
        (2, 'Shipped'),
        (3, 'Cancel'),
        (4, 'Delivered'),
        (5,'Returned')
    )
    status = models.SmallIntegerField( choices=STATUS_CHOICES, default=1)
    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name + " has ordered with orderId " + str(self.order_id)
    

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveBigIntegerField(default=0)

class OrderCancel(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    date = models.DateField(default=now)
    reason = models.CharField(max_length=200,null=True,blank=True)
    class Meta:
        verbose_name = "Cancel Order"
    def __str__(self):
        return str(self.order)+" has Canceled "+str(self.date)

class OrderReturn(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    date = models.DateField(default=now)
    reason = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.order)+" has Returned "+str(self.date)
    class Meta:
        verbose_name = "Order Return"

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cm_id')
    review = models.TextField(max_length=100)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timeStamp =models.DateTimeField(default=now)

    def __str__(self) :
        return str(self.feedback_id)
    class Meta:
        unique_together = ("customer", "product", )