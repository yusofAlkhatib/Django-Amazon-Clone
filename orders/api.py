from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Cart , CartDetail , Order , OrderDetail , Coupon
from .serializers import CartDetailsSerializer , CartSerializer , OrderSerializer , OrderDetailSerializer

from settings.models import DeliveryFee
from products.models import Product



class OrderListAPI(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = super(OrderListAPI, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
    # def list(self, request, *args, **kwargs):
    #     queryset = super().list(request, *args, **kwargs)
    #     queryset = queryset.filter(user=self.request.user)
    #     return queryset
    
    


class OrderDetailAPI(generics.RetrieveAPIView):
    pass
    


class CreateOrderAPI(generics.GenericAPIView):
    pass



class ApplyCouponAPI(generics.GenericAPIView):
    pass



class CartCreateUpdateDeleteAPI(generics.GenericAPIView):
    pass