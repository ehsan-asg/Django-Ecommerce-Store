from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from core.models import BaseModel

class User(AbstractBaseUser,PermissionsMixin):
	email = models.EmailField(max_length=255, unique=True , null=True,blank=True)
	phone_number = models.CharField(max_length=11, unique=True)
	full_name = models.CharField(max_length=200)
	role = models.CharField(max_length=50,null=True)
	image_profile = models.ImageField(upload_to ='uploads/% Y/% m/% d/',null=True,blank=True) 
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True,null=True)
	updated_at = models.DateTimeField(auto_now=True)
	


	objects = UserManager()

	USERNAME_FIELD = 'phone_number'
	REQUIRED_FIELDS = ['email', 'full_name']

	def __str__(self):
		return self.full_name
	@property
	def is_staff(self):
		return self.is_admin

class OtpCode(BaseModel):
	phone_number = models.CharField(max_length=11, unique=True)
	code = models.PositiveSmallIntegerField()

	def __str__(self) -> str:
		return f"{self.phone_number} - {self.code} - {self.created_at}"
