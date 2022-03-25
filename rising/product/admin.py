import datetime

from django.contrib import admin
from django.shortcuts import render
from django.utils.timezone import now
from django_xhtml2pdf.utils import pdf_decorator

from .models import *


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_id','category_name','subcategory']
	ordering = ('category_id',)

class ProductAdmin(admin.ModelAdmin):
	list_per_page = 8
	search_fields = ('product_name','category', 'subcategory')
	list_filter = ['category']
	list_display =('product_id','product_name','category','quntity','price')
	ordering = ('product_id',)
	

	@admin.action(description='Get Report')
	@pdf_decorator(pdfname='Product Report.pdf')
	def GeneratePdf(modeladmin, request, queryset):
		currentdate = now
		products = queryset
		return render(request, 'report/product-report.html',{'products':products,'currentdate': currentdate})

	actions = [GeneratePdf]

class Product_ImgAdmin(admin.ModelAdmin):
	list_per_page = 8


class OrderDetailInline(admin.TabularInline):
	model = OrderDetail
	extra = 0

	def has_add_permission(self, request, obj = None):
		return False
	def has_delete_permission(self, request, obj = None):
		return False
	def has_change_permission(self, request, obj=None):
		return False

class OrderAdmin(admin.ModelAdmin):
	list_per_page = 8
	list_filter = ['status']
	search_fields = ['name']
	inlines  = [OrderDetailInline]
	list_display =('order_id','order_date','name','amount','status')
	ordering = ('-order_date',)
	date_hierarchy = 'order_date'
	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj = None):
		return False
	readonly_fields = ['order_id','order_date','amount','name','email','phone','city','state','pin_code','address','customer','razorpay_order_id','razorpay_payment_id','razorpay_signature']
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(Delivery_boy=request.user)

	def formfield_for_foreignkey(self, db_field, request, **kwargs) :
		if db_field.name =='Delivery_boy':
			if not request.user.is_superuser:
				kwargs['queryset'] = User.objects.filter(id=request.user.id)
		return super().formfield_for_foreignkey(db_field, request, **kwargs)
		
	@admin.action(description='Get Report')
	@pdf_decorator(pdfname='Order  Report.pdf')
	def GeneratePdf(modeladmin, request, queryset):
		currentdate = now
		orders = queryset
		return render(request, 'report/order-report.html',{'orders':orders,'currentdate': currentdate})

	actions = [GeneratePdf]
	

class FeedbackAdmin(admin.ModelAdmin):
	list_filter = ['timeStamp']
	list_display =["feedback_id","customer","rating","product"]
	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj = None):
		return False
	def has_change_permission(self, request, obj=None):
		return False

class CancelOrderAdmin(admin.ModelAdmin):
	list_display = ['id','order','date']
	ordering = ('-date',)
	date_hierarchy = 'date'
	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj = None):
		return False
	def has_change_permission(self, request, obj=None):
		return False
	
	@admin.action(description='Get Report')
	@pdf_decorator(pdfname='Order Cancel Report.pdf')
	def GeneratePdf(modeladmin, request, queryset):
		currentdate = now
		orders = queryset
		return render(request, 'report/order-cancel-report.html',{'orders':orders,'currentdate': currentdate})

	actions = [GeneratePdf]	

class OrderReturnAdmin(admin.ModelAdmin):
	list_display = ['id','order','date']
	ordering = ('-date',)
	date_hierarchy = 'date'
	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj = None):
		return False
	def has_change_permission(self, request, obj=None):
		return False

	@admin.action(description='Get Report')
	@pdf_decorator(pdfname='Order Return Report.pdf')
	def GeneratePdf(modeladmin, request, queryset):
		currentdate = now
		orders = queryset
		return render(request, 'report/order-return.html',{'orders':orders,'currentdate': currentdate})

	actions = [GeneratePdf]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(OrderCancel,CancelOrderAdmin)
admin.site.register(OrderReturn,OrderReturnAdmin)

