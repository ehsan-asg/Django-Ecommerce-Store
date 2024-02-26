from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
import random
from rest_framework.permissions import IsAuthenticated
from utils import send_otp_code
from .models import OtpCode,User
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import UserRegisterSerializers,UserRegisterVerifyCode,UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
#Template
class UserAddAddress(View):
    template_name = 'accounts/register.html'
class UserRegisterView(TemplateView):
    template_name = 'accounts/register.html'

class UserVerifyCodeView(TemplateView):
    template_name = 'accounts/verify-code.html'

class UserLoginCodeView(TemplateView):
    template_name = 'accounts/login.html'

class UserProfileTemplateView(TemplateView):
    template_name = 'accounts/profile.html'

#Api
class UserRegister(APIView):
    
    def post(self,request):
        random_code = random.randint(1000, 9999)
        ser_data = UserRegisterSerializers(data=request.POST)
        if ser_data.is_valid():
            send_otp_code(ser_data.validated_data['phone_number'],random_code)
            OtpCode.objects.create(phone_number=ser_data.validated_data['phone_number'], code=random_code)
            request.session['user_registration_info'] = {
				'phone_number': ser_data.data['phone_number'],
				'full_name': ser_data.data['full_name'],
				'password': ser_data.data['password'],
			}
            return Response({'user':ser_data.data,'otp_code': random_code}, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserVerifyCode(APIView):
    def post(self,request):
        ser_data = UserRegisterVerifyCode(data=request.data)
        if ser_data.is_valid():
            user_session = request.session['user_registration_info']
            code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
            if ser_data.data['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'],user_session['full_name'], user_session['password'])
                OtpCode.objects.filter(phone_number=user_session['phone_number']).delete()
                return Response({'message': 'Thanks for signing up. Your account has been created.'}, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAllView(APIView):
    serializer_class = UserSerializer
    def get(self, request):
        serializer = self.serializer_class(User.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

