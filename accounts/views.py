from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegisterForm,VerifyCodeForm
import random
from utils import send_otp_code
from .models import OtpCode,User
from django.contrib import messages
from rest_framework.views import APIView
from .serializers import UserRegisterSerializers
from rest_framework import status
from rest_framework.response import Response

class UserRegister(APIView):
    def post(self,request):
        ser_data = UserRegisterSerializers(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm
    def get(self,request):
        form = self.form_class
        return render(request,'accounts/verify-code.html',{'form':form})

    def post(self,request):
        user_session = request.session['user_register_info']
        code_instance = OtpCode.objects.get(phone_number = user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data['code']
            if code_instance.code == cd:
               User.objects.create(phone_number=user_session['phone_number'],full_name=user_session['full_name'],password=user_session['password'])
               code_instance.delete()
               messages.success(request,"you register","susccess")
            else:
                messages.error(request,"this code is wrong",'danger')
                return redirect('accounts:accounts-verify')
        return redirect('accounts:accounts-register')
class ProfileView(View):
    def get(self,request):
        return render(request,"accounts/profile.html")