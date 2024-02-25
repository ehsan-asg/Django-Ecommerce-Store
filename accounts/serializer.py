from rest_framework import serializers
from .models import OtpCode
from django.contrib.auth import password_validation
from django.contrib.auth import get_user_model




class UserRegisterSerializers(serializers.ModelSerializer):
    
	class Meta:
		model = get_user_model()
		fields = ('phone_number', 'full_name', 'password')

	def validate_username(self, value):
		if value == 'admin':
			raise serializers.ValidationError('username cant be `admin`')
		return value

	def validate_password(self, value):
         password_validation.validate_password(value, self.instance)
         return value
	
class UserRegisterVerifyCode(serializers.ModelSerializer):
	class Meta:
		model = OtpCode
		fields = ('code',)
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = "__all__"