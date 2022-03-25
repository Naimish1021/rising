from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ProductHome'),
    path("<int:myid>", views.productView, name="ProductView"),
    path('orderdetail',views.orderDetail, name="TrackerStatus"),
    path('search', views.search, name="Search"),
    path('checkout', views.checkout, name="Checkout"),
    path('cart', views.cart, name="ViewCart"),
    path('update_cart',views.update_cart, name='Cart'),
    path('cancel/<int:id>', views.productCancel, name="ProductCancel"),
    path('success/<int:id>', views.success, name="Success"),
    path('order_invoice/<int:id>', views.orderInvoice, name="OrderInvoice"),
    path('postFeedback', views.postFeedback, name="PostFeedback"),
    path('return/<int:id>',views.productReturn,name="ProductReturn")

]
