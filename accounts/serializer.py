from rest_framework import serializers
from .models import OtpCode
from django.contrib.auth import password_validation
from django.contrib.auth.models import User


class UserRegisterSerializers(serializers.ModelSerializer):
    
	class Meta:
		model = User
		fields = ('phone_number', 'full_name', 'password')

	def create(self, validated_data):
		return User.objects.create_user(**validated_data)

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
		model = User
		fields = "__all__"