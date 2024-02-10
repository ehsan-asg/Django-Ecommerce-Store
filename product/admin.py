from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Product,Category,Feature

@admin.register(Product)
class Productadmin(admin.ModelAdmin):
      list_display = ['name','available','created_at','updated_at']
      list_filter = ('created_at','available')
      search_fields = ('name',)
      ordering = ('created_at',)
@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
      list_display = ['name','is_sub','created_at','updated_at']
      search_fields = ('name',)
      ordering = ('created_at',)
@admin.register(Feature)
class Featureadmin(admin.ModelAdmin):
      list_display = ['name','value','price','created_at','updated_at']
      search_fields = ('name',)
      ordering = ('created_at',)
class Discount(admin.ModelAdmin):
      list_display = ['title','type','amount','valid_from','valid_to','active','created_at']
      search_fields = ('title','amount')
      ordering = ('created_at',)

