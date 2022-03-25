from pyexpat import model
from django.contrib import admin
from .models import *
from django.utils.html import format_html
from datetime import date
from django_xhtml2pdf.utils import pdf_decorator 
from django.utils.timezone import now
import datetime
from django.shortcuts import render

class PackageBookingAdmin(admin.ModelAdmin):
	list_display = ('booking_id','customer','noOfPerson','booking_date','package',)
	list_filter = ('package','status')
	date_hierarchy ='booking_date'
	ordering = ('-booking_date',)
	search_fields = ('customer','package')

	
	@admin.action(description='Get Report')
	@pdf_decorator(pdfname='Package Report.pdf')
	def GeneratePdf(modeladmin, request, queryset):
		currentdate = datetime.datetime.now
		packages = queryset
		return render(request, 'report/booking-report.html',{'bookings':packages,'currentdate': currentdate})

	actions = [GeneratePdf]

	# def has_add_permission(self, request):
	# 	return False
	# def has_delete_permission(self, request, obj = None):
	# 	return False
	# def has_change_permission(self, request, obj=None):
	# 	return False


class PackageDateInline(admin.TabularInline):
	model = PackageDate
	extra =0

   

class JoinFromInline(admin.TabularInline):
	model = JoinFrom
	extra = 0
	
class ScheduleInline(admin.TabularInline):
	model = Schedule
	extra = 0



@admin.register(Package)  
class PackageAdmin(admin.ModelAdmin):
	model = Package
	inlines = [PackageDateInline,JoinFromInline,ScheduleInline]
	list_display = ['id','name','days','nights','amount']
	ordering = ['id']
	search_fields = ('name',)
	list_per_page = 8

	@admin.action(description='Get Report')
	@pdf_decorator(pdfname='Package Report.pdf')
	def GeneratePdf(modeladmin, request, queryset):
		currentdate = datetime.datetime.now
		packages = queryset
		return render(request, 'report/package-report.html',{'packages':packages,'currentdate': currentdate})

	actions = [GeneratePdf]

class ScheduleAdmin(admin.ModelAdmin):
	list_display = ('package','dayNo','placeCaption')
	list_filter = ('package',)
	ordering = ('package','dayNo')
	search_fields = ('package',)
	list_per_page = 8

class PackageDateAdmin(admin.ModelAdmin):
	list_display = ('package','date','guide','maxPerson')
	list_filter = ('package',)
	date_hierarchy ='date'
	search_fields = ('package','date')
	ordering =('package','date')
	list_per_page = 8

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(guide=request.user)

	@admin.action(description='Get Report')
	@pdf_decorator(pdfname='Package Booking Report.pdf')
	def GeneratePdf(modeladmin, request, queryset):
		currentdate = datetime.datetime.now
		dates = queryset
		return render(request, 'report/package-booking-report.html',{'dates':dates,'currentdate': currentdate})
	actions = [GeneratePdf]
	
class VisitAdmin(admin.ModelAdmin):
	list_display =('id','place_name','address','city')
	ordering=('id',)
	search_fields = ('place_name','city')
	list_per_page = 8


class PackageCancelAdmin(admin.ModelAdmin):
	list_display=['id','booking','date']
	ordering = ('-date',)
	list_per_page = 8

	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj = None):
		return False
	def has_change_permission(self, request, obj=None):
		return False

	@admin.action(description='Get Report')
	@pdf_decorator(pdfname='Package Booking Cancel Report.pdf')
	def GeneratePdf(modeladmin, request, queryset):
		currentdate = datetime.datetime.now
		canceldates = queryset
		return render(request, 'report/package-booking-cancel-report.html',{'canceldates':canceldates,'currentdate': currentdate})
	actions = [GeneratePdf]

class JoinFromAdmin(admin.ModelAdmin):
	list_per_page = 8
		
admin.site.register(Package_Booking,PackageBookingAdmin)
admin.site.register(Offer)
admin.site.register(Visit_Place,VisitAdmin)
admin.site.register(JoinFrom, JoinFromAdmin)
admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(PackageDate,PackageDateAdmin)
admin.site.register(PackageCancel,PackageCancelAdmin)
