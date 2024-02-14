from django.contrib import admin
from .models import Coupon,Order,OrderItem,Address
from django.contrib.auth import get_user_model

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code','discount','active','valid_from','valid_to','created_at']
    list_filter = ('code','created_at')
    ordering = ('created_at',)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','created_at','updated_at']
    list_filter = ('created_at',)
    ordering = ('created_at',)
    inlines = (OrderItemInline,)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [get_user_model,"created_at","updated_at"]
    list_filter = ('created_at',"state","city")
    ordering = ('created_at',)

