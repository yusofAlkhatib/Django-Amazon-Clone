from django.urls import path
from .views import add_to_cart,order_list,checkout,process_payment,payment_success,payment_failed
from .api import OrderDetailAPI , OrderListAPI , ApplyCouponAPI , CartCreateUpdateDeleteAPI , CreateOrderAPI


urlpatterns = [
    
     path('' , order_list),
     path('checkout/' , checkout),
     path('checkout/process_payment' , process_payment),
     path('checkout/payment_success' , payment_success),
     path('checkout/payment_failed' , payment_failed),
     path('add-to-cart' , add_to_cart),

     # apis
     path('api/<str:username>/orders', OrderListAPI.as_view()),
     path('api/<str:username>/orders/<int:pk>', OrderDetailAPI.as_view()),
     path('api/<str:username>/orders/create-order', CreateOrderAPI.as_view()),
     path('api/<str:username>/cart', CartCreateUpdateDeleteAPI.as_view()),
     path('api/<str:username>/apply-coupon', ApplyCouponAPI.as_view()),
]
