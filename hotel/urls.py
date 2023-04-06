from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^cart/$', views.cart, name='cart'),
    path(r'^menu/$', views.menu, name='menu'),
    path(r'^myorders/$', views.my_orders, name='my_orders'),
    
    path(r'^dashboard/admin/users/$', views.users_admin, name='users_admin'),
    path(r'^dashboard/admin/orders/$', views.orders_admin, name='orders_admin'),
    path(r'^dashboard/admin/foods/$', views.foods_admin, name='foods_admin'),
    path(r'^dashboard/admin/$', views.dashboard_admin, name='dashboard_admin'),
    path(r'^dashboard/admin/sales/$', views.sales_admin, name='sales_admin'),
    
    path(r'^dashboard/admin/users/add_user/$', views.add_user, name='add_user'),
    path(r'^dashboard/admin/foods/add_food/$', views.add_food, name='add_food'),
    path(r'^dashboard/admin/sales/add_sales/$', views.add_sales, name='add_sales'),
    path(r'^dashboard/admin/foods/editFood/(?P<foodID>\d+)/$', views.edit_food, name='edit_food'),
    path(r'^dashboard/admin/foods/foodDetails/(?P<foodID>\d+)/$', views.food_details, name='food_details'),
    path(r'^dashboard/admin/sales/editSale/(?P<saleID>\d+)/$', views.edit_sales, name='edit_sales'),
    
    path(r'^dashboard/admin/orders/confirm_order/(?P<orderID>\d+)/$', views.confirm_order, name='confirm_order'),
    path(r'^dashboard/admin/orders/confirm_delivery/(?P<orderID>\d+)/$', views.confirm_delivery, name='confirm_delivery'),
    
    path(r'^delete_item/(?P<ID>\d+)/$', views.delete_item, name='delete_item'),
    path(r'^add_deliveryBoy/(?P<orderID>\d+)/$', views.add_deliveryBoy, name='add_deliveryBoy'),
    path(r'^placeOrder/$', views.placeOrder, name='placeOrder'),
    path(r'^addTocart/(?P<foodID>\d+)/(?P<userID>\d+)/$', views.addTocart, name='addTocart'),

    path(r'^dashboard/delivery_boy/$', views.delivery_boy, name='delivery_boy'),
]
