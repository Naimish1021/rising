from struct import pack
from package.models import Package_Booking
from .models import Order
from package.models import Notificaton
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.db.models import Q
def NoofOrder(request):

    total_order =  Order.objects.exclude(status =3 ).count()
    orders =Order.objects.exclude(Q(status = 3)|Q(status = 5))
    total_order_amount= 0
    
    for order in orders:
        total_order_amount  += order.amount

    total_tour =  Package_Booking.objects.exclude(status=3).count()
    allPackage = Package_Booking.objects.exclude(status=3)
    total_tour_amount = 0
    notifications = Notificaton.objects.filter(is_seen = False)
    
    for package in allPackage:
        total_tour_amount += package.amount
    
    return {
        'total_order': total_order,
        'total_order_amount':total_order_amount,
        'total_tour': total_tour,
        'total_tour_amount': total_tour_amount,
        'notifications':notifications,
    }

 
