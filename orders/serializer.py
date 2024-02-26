from rest_framework import serializers
from .models import Coupon,Order,OrderItem,Address
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


class CouponSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"
class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['user']

    def create(self, validated_data):
        user_session = self.context['request'].session['user_registration_info']
        user_instance = get_object_or_404(get_user_model(), phone_number=user_session['phone_number'])
        address_instance = Address.objects.create(user=user_instance, **validated_data)
        
        return address_instance