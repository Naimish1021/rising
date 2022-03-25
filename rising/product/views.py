
from urllib import request
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from math import  ceil
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import razorpay
from product.models import *
from package.models import Notificaton
from account.models import User
from django.contrib.auth.decorators import login_required
from rising.settings import MID, MKEY
from django.contrib import messages
from django.db.models import Avg
import datetime
from datetime import timedelta
from django_xhtml2pdf.utils import pdf_decorator



# Create your views here.

def index(request):

	# return HttpResponse('This is product index page')
	allprods = []
	catprods = Product.objects.values('category', 'product_id')

	cats = {item['category'] for item in catprods}
	for cat in cats:
		prods = Product.objects.filter(category = cat)
		n = len(prods)
		nSlides = n // 4 + ceil((n / 4) - (n // 4))
		allprods.append([prods, range(1, nSlides), nSlides])

	user = request.user
	params = {
		'allprods': allprods, 
		'user' : user,
		}
	
	return render(request, 'product/index.html', params)


def orderDetail(request):
	orders = Order.objects.filter(customer=request.user).order_by('-order_id')
	return render(request,'product/tracker.html',{'orders':orders})


def searchMatch(query, item):
	''' return true only if query mathches the item'''
	if query in item.description.lower() or query in item.product_name.lower():
		return True
	else:   
		return False

def search(request):
	query = request.GET.get('search')
	allprods = []
	catprods = Product.objects.values('category', 'product_id')
	cats = {item['category'] for item in catprods}
	for cat in cats:
		prodtemp = Product.objects.filter(category = cat)
		prod = [item for item in prodtemp if searchMatch(query, item) ]
		n = len(prod)
		nSlides = n // 4 + ceil((n / 4) - (n // 4))
		if len(prod) != 0:
			allprods.append([prod, range(1, nSlides), nSlides])  
	params = {'allprods': allprods, 'msg': ""}
	if len(allprods) == 0 or len(query) < 3:
		params['msg'] = "Results not found. Please enter valid search."
	return render(request, 'product/search.html', params)

def productView(request, myid):
	if request.method == 'GET':
		user = request.user
		#Fetch the product using the id
		product=Product.objects.get(product_id = myid)
		feedbacks = Feedback.objects.filter(product=product)
		
		# ratings = Rating.objects.filter(product_id = myid)
		# for rating in ratings:
		avg_rating = Feedback.objects.filter(product=product).aggregate(Avg("rating"))
		if avg_rating != None:
			rating = avg_rating['rating__avg']
		else:
			rating = 0
		is_feedback =True

		if request.user.is_authenticated: 
			order = Order.objects.filter(customer=user,status=4)
			for item in order:
				if OrderDetail.objects.filter(order=item,product_id=product).exists() :
					is_feedback = Feedback.objects.filter(product=product,customer=user).exists()
					break
		
		params =  {
			'product':product,
			'feedbacks' : feedbacks,
			'rating' : rating,
			'is_feedback':is_feedback,
		}
		return render(request, "product/productView.html", params)
	   
def checkout(request):
	global payment
	user = request.user
	
	if request.method=="POST":
		user = request.user
		customer = User.objects.get(id = user.id)
		items = Cart.objects.filter(user_id = user.id)
		name = request.POST.get('name', '')
		amount = request.POST.get('amount')
		email = request.POST.get('email', '')
		phone = request.POST.get('phone', '')
		address = request.POST.get('address')
		city = request.POST.get('city', '')
		state = request.POST.get('state', '')
		zip_code = request.POST.get('pincode', '')
		
		order = Order(name=name, phone=phone, email=email, address= address, city = city, state=state, pin_code=zip_code, amount=amount, customer = customer)

		client = razorpay.Client(auth=(MID, MKEY))

		data = { "amount": int(order.amount)*100, "currency": "INR", "receipt": str(order.order_id) }
		payment = client.order.create(data=data)
		payment = dict(payment)
		order.razorpay_order_id = payment['id']
		order.save()
		for item in items:
			product = item.product_id
			product.quntity -= item.quantity
			product.save()
			order_detail = OrderDetail(order= order,product_id = item.product_id,price=item.price,quantity=item.quantity)
			order_detail.save()
			item.delete()
		notificaton = Notificaton(type=2,pid=order.order_id)
		notificaton.save()
		

		email = order.email
		name = order.name
		amount = order.amount
		orderdate = order.order_date
		date = orderdate.strftime("%d-%m-%Y")
		sender_email = "chanchadkeyur@gmail.com"  # Enter your address
		receiver_email = (str(email),)  # Enter receiver address
		password = "keyur21112001"
		message = f"\nSubject: Hi {name} \n \t Thank you for ordering from Rising Adventure E-cart. You have successfully order product and we get it product amount {amount}₹.\n order date:{date}\n We will deliver as soon as posible.\n \n \t \t \t Thank you {name}"

		subject = f"Your Order placed sucessfully ."
		send_mail(subject, message, sender_email, receiver_email, fail_silently=True)

		# Request Razorpay to transfer amount to your account after Payment by user.     
		params = {
			'payment':payment, 
			'orderId':order.razorpay_order_id, 
			'order_id':order.order_id,
			'order': order
			}
		return render(request, 'product/payment.html', params)

	customer = User.objects.get(id=user.id)
	carts = Cart.objects.filter(user_id=customer)
	amount=0
	for cart in carts:
		amount += cart.price

	params = {
		'cart': carts,
		'amount':amount,
		'customer':customer,
	}
	return render(request, 'product/checkout.html',params) 
	

def cart(request):
	user = request.user
	# if request.is_ajax() and request.method == 'GET':
	#     pass 
	if request.method == 'GET':
		carts = Cart.objects.filter(user_id = user.id)
		total = 0
		for cart in carts:
			total += cart.price
		return render(request, 'product/cart.html',{'carts' : carts, 'total':total,})

def update_cart(request):
	if request.method == 'POST':
		user = request.user
		action = request.POST.get('method')
		productid = int( request.POST.get('product_id') )
		qty = int( request.POST.get('qty') )
		p_user = User.objects.get(id = user.id)

		if productid != 0 and productid !=None and action != "fullclear":
			if action == "remove":
				cart = Cart.objects.get(user_id =p_user,product_id = productid)
				cart.delete()
				carts = Cart.objects.filter(user_id = user.id)
				request.session['cart']=Cart.objects.filter(user_id=request.user).count()
				total = 0
				for cart in carts:
					total += cart.price
				return HttpResponse(total)

			else:
				product = Product.objects.get(product_id = productid)
				price = product.price * qty
				cart , created = Cart.objects.get_or_create(user_id =p_user, product_id = product)
				if qty >0:
					cart.quantity = qty
					cart.price = price
					cart.save()
					carts = Cart.objects.filter(user_id = user.id)
					total = 0
					for cart in carts:
						total += cart.price
						
					response = json.dumps( {'subtotal':price, 'total':total}, default=str )
					request.session['cart']=Cart.objects.filter(user_id=request.user).count()
					return HttpResponse(response)
				else:
					
					cart.delete()
					request.session['cart']=Cart.objects.filter(user_id=request.user).count()
					return HttpResponse('product gone from cart')
			
		else:
			try:
				carts = Cart.objects.filter(user_id = p_user)
				for cart in carts:
					cart.delete()
					request.session['cart']=Cart.objects.filter(user_id=request.user).count()
				return HttpResponse('all cart clear')
			except:
				return HttpResponse('error to all cart clear')

# order = Order.objects.filter(order_id = 28, email = 'chanchadkeyur@gmail.com').first()
# print(order)
# orderDate = order.order_date
# print(orderDate)
# if orderDate + timedelta(days=2)   < datetime.datetime.now():
#     print('yes')
# else:
#     print('no')


def productCancel(request,id):
	
	if request.method =="POST":
		reason = request.POST.get('reason')
		id = request.POST.get('id')

		order = Order.objects.get(order_id =id)
		order.status = 3
		order.save()
		orderdetail=OrderDetail.objects.filter(order=order)
		for item in orderdetail:
			product = item.product_id
			product.quntity += item.quantity
			product.save()

		cancelorder = OrderCancel(order=order,reason=reason)
		cancelorder.save()
		notificaton = Notificaton(type=3,pid=cancelorder.id)
		notificaton.save()
		messages.info(request,"your order is cancelled")
		return redirect('TrackerStatus')
	
	order = Order.objects.get(order_id=id,customer=request.user)
	return render(request, 'product/cancel.html',{'order':order})

def productReturn(request,id):
	if request.method =="POST":
		reason = request.POST.get('reason')
		id = request.POST.get('id')

		order = Order.objects.get(order_id =id)
		order.status = 3
		order.save()
		orderdetail=OrderDetail.objects.filter(order=order)
		for item in orderdetail:
			product = item.product_id
			product.quntity += item.quantity
			product.save()

		returnorder = OrderReturn(order=order,reason=reason)
		returnorder.save()
		notificaton = Notificaton(type=4,pid=returnorder.id)
		notificaton.save()
		messages.info(request,"your order return request is sent")
		return redirect('TrackerStatus')
	
	order = Order.objects.get(order_id=id,customer=request.user)
	return render(request, 'product/return.html',{'order':order})
	
	
@pdf_decorator(pdfname='Order_Invoice.pdf')
def orderInvoice(request,id):
	
	order = Order.objects.get(order_id =id)
	orderdetail = OrderDetail.objects.filter(order = order)
	currentdate = datetime.datetime.now
	total = 0
	for item in orderdetail:
		total += item.price
	return render(request, 'report/orderInvoice.html',{'carts':orderdetail ,'order':order, 'total':total, 'currentdate':currentdate})

def success(request,id):
	orderInvoice(request,id)
	request.session['cart']=0
	return render(request, 'product/success.html')

def postFeedback(request):
	if request.method == 'POST':
		user = request.user
		feedback = request.POST.get("feedback")
		rating = request.POST.get("rating")
		
		pid = request.POST.get("pid")
		product = Product.objects.get(product_id=pid) 
		
		comment=Feedback(review=feedback, customer=user, product=product,rating=rating)
		comment.save()
		messages.success(request, "Your feedback has been posted successfully")


		return redirect(f"/product/{product.product_id}")
