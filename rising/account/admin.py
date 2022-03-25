from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .form import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'first_name','last_name','date_joined','role','last_login')
    list_filter = ('email', 'role',)
    fieldsets = (
        (('Personal info'), {'fields': ('first_name', 'last_name', 'mobile','address','city')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff','role','groups'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    readonly_fields = ['email', 'date_joined','last_login','first_name', 'last_name', 'mobile','address','city']
    search_fields = ('email','first_name','last_name')
    ordering = ('email',)
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj = None):
        return False
    def has_change_permission(self, request, obj=None):
        return True

class CityAdmin(admin.ModelAdmin):
    list_display = ['city_id','city_name','state']
    search_fields =['city_id','city_name','state']
    list_filter = ['state']
    ordring = ['city_id']
    list_per_page = 8

class StateAdmin(admin.ModelAdmin):
    list_display = ['state_id','state_name']
    search_fields = ['state_name']
    ordring = ['state_id']
    list_per_page = 8




admin.site.register(User, CustomUserAdmin)

admin.site.register(State, StateAdmin)
admin.site.register(City,CityAdmin)