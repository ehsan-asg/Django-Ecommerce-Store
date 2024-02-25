from rest_framework import serializers
from .models import Coupon,Order,OrderItem,Address

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
        fields = "__all__"