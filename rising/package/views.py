from ast import Return
import email
from django.forms import DateInput
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from account.models import User
from product.models import Order, Cart, OrderCancel
from . models import *
import razorpay
import datetime
from django.core.mail import send_mail
from .forms import *
from django_xhtml2pdf.utils import pdf_decorator 
from datetime import timedelta

import math, random
# APIs Views 
def index(request):
	if request.user.is_authenticated:
		request.session['cart']=Cart.objects.filter(user_id=request.user).count()
		
	else:
		request.session['cart']=0

	bookings = Package_Booking.objects.exclude(status=3)
	for booking in bookings:
		if booking.package.date < now().date():
			booking.status = 2
			booking.save()
	packages = Package.objects.all()[:11]
	allPackages = {'allPackages' : packages}
	return render(request, 'package/index.html', allPackages)

def events(request):
	packages = Package.objects.all()
	allPackages = {'allPackages' : packages}
	return render(request, 'package/events.html',allPackages)

def eventInfo(request, id):
	if request.method == "GET":
		package = Package.objects.get(id = id)
		join_us = JoinFrom.objects.filter(package = package)
		schedules = Schedule.objects.filter(package=package).order_by('dayNo')

		package = {
			'package' : package,
			'schedules' : schedules, 
			'join_us' : join_us,
			}
		return render(request, 'package/event-slug.html', package)

@login_required(login_url="/login")
def packageview(request, id):
	global payment
	user = request.user
	if request.method == 'GET':
		package = Package.objects.get(id = id)
		join_us = JoinFrom.objects.filter(package = package)
		dates = PackageDate.objects.filter(package = package,date__gte = now(),maxPerson__gte=1 )
		# join_us = Join_From.objects.filter(package = package)[:1]
		package = {
			'package' : package,
			'join_us' : join_us,
			'dates' : dates,
			
		}
		return render(request, 'package/packageView.html', package)

	
	if request.method=="POST":
		user = request.user
		name = request.POST.get('name', '')
		id = request.POST.get('id')
		noofperson =request.POST.get('noofperson')
		dateid = request.POST.get('date')
		email = request.POST.get('email', '')
		phone = request.POST.get('phone', '')
		address = request.POST.get('address', '')
		city = request.POST.get('city', '')
		state = request.POST.get('state', '')
		zip_code = request.POST.get('pincode', '')

		joinFrom = JoinFrom.objects.get(id=id) 
		package = PackageDate.objects.get(id=dateid)
		if int(noofperson) >package.maxPerson:
			messages.error(request, 'This package is have only that much '+str(package.maxPerson)+' person can join \n please select other package date')
			return HttpResponseRedirect(request.path_info)

		package.maxPerson =package.maxPerson -int(noofperson)
		package.save()
		total = int(noofperson)*int(joinFrom.amount)
		
		# formating string to date
	
		booking = Package_Booking(package=package,joinFrom=joinFrom,noOfPerson=noofperson, name=name, phone=phone, email=email, address= address, city = city, state=state, pin_code=zip_code, amount=total,status=1,customer=user)
		booking.save()   

		 # Request Razorpay to transfer amount to your account after Payment by user.     
		client = razorpay.Client(auth=("rzp_test_CbBqgB9J6EAyeg", "QphQBGO4tQgLluKNDJokLGL8"))

		data = { "amount": int(booking.amount)*100, "currency": "INR", "receipt": str(booking.booking_id) }
		
		payment = client.order.create(data=data)
		payment = dict(payment)
		booking.razorpay_booking_id = payment['id']
		booking.save()
		notificaton = Notificaton(type=1,pid=booking.booking_id)
		notificaton.save()
		params = {
			'payment':payment, 
			'bookingId':booking.razorpay_booking_id, 
			'booking_id':booking.booking_id,
			'booking': booking
			}
		
		return render(request, 'package/payment.html', params)

def aboutUs(request):
	return render(request, 'package/about-us.html')

def searchMatch(query, item):
	''' return true only if query mathches the item'''
	if query in item.description.lower() or query in item.name.lower() or query in item.slug.lower():
		return True
	else:   
		return False

def search(request):
	query = request.GET.get('search')
	allpckgs = []
	pckgTmp = Package.objects.all() 
	allpckgs = [item for item in pckgTmp if searchMatch(query, item) ] 
	params = {'allpckgs': allpckgs, 'msg': ""}
	if len(allpckgs) == 0 or len(query) < 3:
		params['msg'] = "Results not found. Please enter valid search."
	return render(request, 'package/search.html', params)


def packageCancel(request,id):

	if request.method =="POST":
		reason = request.POST.get('reason')
		id = request.POST.get('id')

		order = Package_Booking.objects.get(booking_id =id)
		order.status = 3
		order.save()
		package = order.package
		package.maxPerson += order.noOfPerson
		package.save()
		cancelorder =PackageCancel(booking=order,reason=reason)
		cancelorder.save()
		notificaton = Notificaton(type=5,pid=cancelorder.id)
		notificaton.save()

		
		email = order.email
		name = order.name
		package = order.package.package.name
		amount = order.amount
		sender_email = "chanchadkeyur@gmail.com"  # Enter your address
		receiver_email = (str(email),)  # Enter receiver address
		password = "keyur21112001"
		message = f"\nSubject: Hi {name} \n \t You have been cancel your package {package} of rising adventure. We will transfer package amount {amount}₹ in your razorpay account.\n \n \t \t \t Thank you {name}"
		subject = f"About your package cancel."
		send_mail(subject, message, sender_email, receiver_email, fail_silently=True)

		messages.info(request,"Your package is cancelled.")
		return redirect('MyPackage')

	booking = Package_Booking.objects.get(booking_id=id)

	return render(request, 'package/cancel.html',{'booking':booking})


def contact1(request):  

	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['mail']
		phone = request.POST['phone']
		address = request.POST['address']
		message = request.POST['messageForm']

		contact = Contact(name=name, email=email, phone=phone, address=address, message=message)
		contact.save()
		messages.success(request, 'Your message has been sent successfully.')
		return render(request, 'package/contact-1.html')

	
	return render(request, 'package/contact-1.html')

def error404(request):
	return render(request, 'package/Error404.html')




# APIs Views 
def handleLogin(request):
    
    
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method=="POST":
        # Get the post parameters
        page=request.POST['page']
        username = request.POST['email']
        password = request.POST['logpass']
        
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
              
                
                if user.is_superuser:
                    return redirect('/admin')
                else:
                    return redirect(page)
               
            else:
                messages.info(request, 'Email OR password is incorrect')
                return redirect('/login?next='+request.GET['next'])
        except:
            messages.error(request, 'Invalid Email and password')
            return redirect('/login?next='+request.GET['next'])


    return render(request, 'package/Error404.html')

def handleSignUp(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    if request.method == "POST":
        # Get the post parameters
        page = request.POST['page']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        address = request.POST['address']
        page=request.POST['next']
        # check for errorneous input

        if User.objects.filter(email__iexact = email).exists():
            messages.error(request,'Email is already exists')
            return redirect('/signup')
    
          
        user = User.objects.create(email=email,first_name=fname,last_name=lname,mobile=phone,address=address)
        user.set_password(pass1)
        user.save()
        login(request, user)
        
        messages.success(request, 'Your account has been created successfully .')
        return redirect(page)

    return render(request, 'package/Error404.html')

def handleLogout(request):
    logout(request)
    page = request.GET['next']
    return redirect(page)
	
def handleForget(request):
	if request.method == 'GET':
		return render(request, 'forget.html')

	if request.method == 'POST':
		logname = request.POST.get('logname')
		newpass = request.POST.get('newpass')
		conpass = request.POST.get('conpass')
		# user = request.user
		try:
			user = User.objects.get(username = logname)
			if newpass == conpass:
				user.password = newpass
				user.save()
				messages.success(request, 'Your password is forgeted successfully.')
				return redirect('/forget')
		except:
			messages.error(request, 'Username is not exists.')
			return redirect('/forget')



def success(request):
	user = request.user
	
	booked_package = Package_Booking.objects.filter(customer = user).first()
	email = booked_package.email
	name = booked_package.name
	package = booked_package.package.package.name
	amount = booked_package.amount
	eventdate = booked_package.package.date
	sender_email = "chanchadkeyur@gmail.com"  # Enter your address
	receiver_email = (str(email),)  # Enter receiver address
	password = "keyur21112001"
	message = f"\nSubject: Hi {name} \n \t Thank you for booking {package} of rising adventure. You have successfully booked package and package amount {amount}₹ we get it.\n event date:{eventdate}\n We will contact as soon as posible.\n \n \t \t \t Thank you {name}"

	subject = f"About your sucessfully package book."
	send_mail(subject, message, sender_email, receiver_email, fail_silently=True)
	messages.success(request, f"Your package {package} is booked. Check your email.")
	return render(request, 'package/success.html')

def profile(request):
	
	return render(request, 'profile.html')


@pdf_decorator(pdfname='Customer.pdf')
def customer_reports(request):
    currentdate = datetime.datetime.now
    customers = User.objects.filter(role=4)
    return render(request, 'report/customer-report.html',{'customers' : customers, 'currentdate': currentdate})

@pdf_decorator(pdfname='Booking.pdf')
def booking_reports(request):
    currentdate = datetime.datetime.now
    bookings = Package_Booking.objects.exclude(status=3)
    return render(request, 'report/booking-report.html',{'bookings' : bookings, 'currentdate': currentdate})

@pdf_decorator(pdfname='Order.pdf')
def order_reports(request):
    currentdate = datetime.datetime.now
    orders = Order.objects.exclude(status=3)
    return render(request, 'report/order-report.html',{'orders' : orders, 'currentdate': currentdate})

@pdf_decorator(pdfname='Cancel.pdf')
def cancel_reports(request):
    currentdate = datetime.datetime.now
    cancels = OrderCancel.objects.all()
    return render(request, 'report/cancel-report.html',{'cancels' : cancels, 'currentdate': currentdate})



def profileUpdate(request):
	if request.method == "POST":
		fname = request.POST.get("fname")
		lname = request.POST.get("lname")
		mobile = request.POST.get('phone')
		address = request.POST.get('address')
		city = request.POST.get('city')
		state = request.POST.get('state')
		pincode = request.POST.get('pincode')

		user = User.objects.filter(id=request.user.id).update(first_name=fname,last_name=lname,mobile=mobile,address=address,city=city,state=state,pincode=pincode)
		print(user)
		messages.info(request,"Your Profile is Updated")
		return redirect('/user-profile')


def reset_password(request):
	if request.method == "GET":
		return render(request, 'admin/password_reset_done.html')

	if request.method=="POST":
		# Get the post parameters
		
		email = request.POST.get('email')
		password = request.POST.get('password')
		password2 = request.POST.get('confirm-password')
		
		try:
			user = User.objects.get(email= email)
			if password == password2:
				user.set_password(password)
				user.save()
				messages.success(request, 'Password set successfully.')
				return redirect('admin/login')
			else:
				messages.error(request, 'Password and Confirm Password does not match.')
				return redirect('admin/password-resert-done.html')
		except:
			messages.error(request, 'Email does not exits.')
			return redirect('admin/password-reset-done.html')

def mypackage(request):
	packages = Package_Booking.objects.filter(customer=request.user).order_by('-booking_id')
	today =now().date()
	todayPlus5days = today + timedelta(days=5) 
	return  render(request,'package/mypackage.html',{'packages':packages,'today':today, 'todayPlus5days':todayPlus5days})	



def generateOTP() :
	digits = "0123456789"
	OTP = ""
	for i in range(4) :
		OTP += digits[math.floor(random.random() * 10)]
	return OTP

def send_otp(request):
	sender_email = 'chanchadkeyur@gmail.com'
	email=request.POST.get("email")
	receiver_email = str(email,)
	otp=generateOTP()
	print('otpm is' ,otp)
	sender_email = "chanchadkeyur13@gmail.com"
	receiver_email = (str(email),) 
	password = "keyur21112001"


	message = f"Your OTP is {otp}"

	subject = f"OTP request for reset password."
	send_mail(subject, message, sender_email, receiver_email, fail_silently=True)

	return HttpResponse(otp)	


def seenNotification(request):
	if request.method == "POST":
		id = request.POST.get('id')
		notification = Notificaton.objects.get(id = id)
		notification.is_seen=True
		notification.save()
		notification.delete()
		return HttpResponse('notification seen')