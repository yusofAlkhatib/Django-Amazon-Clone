from rest_framework import serializers
from .models import Cart , CartDetail , Order , OrderDetail


class CartDetailSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSeriaizer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'


class OrderDetailSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderSeriaizer(serializers.ModelSerializer):
    order_detail = OrderDetailSeriaizer(many=True)
    class Meta:
        model = Order
        fields = '__all__'
