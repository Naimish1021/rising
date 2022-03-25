from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # APIs for HTML TEMPLATES
    path('', views.index, name="Home"),
    path('events/', views.events, name="Event"),
    path('events/<int:id>', views.eventInfo, name="EventInfo"),
    path('events/<int:id>/packageview', views.packageview, name="packageview"),
    path('about-us', views.aboutUs, name="AboutUs"),
    path('search', views.search, name="Search"),
    path('contact-1', views.contact1, name="Contact1"),
    path('cancel/<int:id>', views.packageCancel, name="PackageCancel"),
    path('error404', views.error404, name="Error404"),
    path('signup', views.handleSignUp, name="Signup"),
    path('login', views.handleLogin, name="Login"),
    path('forget', views.handleForget, name="Forget"),
    path('logout', views.handleLogout, name="Loginout"),
    path('success', views.success, name="Success"),
    path('user-profile', views.profile, name="Profile"),
    path('mypackage', views.mypackage, name="MyPackage"),
    path('customer_reports', views.customer_reports, name="CustomerReports"),
    path('booking_reports', views.booking_reports, name="CustomerReports"),
    path('order_reports', views.order_reports, name="CustomerReports"),
    path('cancel_reports', views.cancel_reports, name="CustomerReports"),
    path('update-profile',views.profileUpdate,name="profileUpdate"),
    # path('mypackage',views.mypackage,name="MyPackage")
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="admin/password_reset.html"),
     name="reset_password"),
    # path('package_invoice/<int:id>',views.package_invoice,name="invoice"),
    path('reset_password_done', views.reset_password, name="password_reset_done"),
    path('notification',views.seenNotification,name="Notification"),
	# path('register/', views.registerPage, name="register"),
   
    path("send_otp",views.send_otp,name="send otp"),
]