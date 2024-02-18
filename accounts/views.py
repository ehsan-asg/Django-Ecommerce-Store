from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegisterForm,VerifyCodeForm
import random
from utils import send_otp_code
from .models import OtpCode,User
from django.contrib import messages

class RegisterUserView(View):
    form_class = UserRegisterForm
    template_class = 'accounts/register.html'
    def get(self,request):
        form = self.form_class 
        return render(request,self.template_class,{'form':form})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000,9999)
            send_otp_code(form.cleaned_data['phone'],random_code)
            OtpCode.objects.create(phone_number = form.cleaned_data['phone'],code=random_code)
            request.session['user_register_info'] = {
                'phone_number':form.cleaned_data['phone'],
                'full_name':form.cleaned_data['full_name'],
                'password':form.cleaned_data['password']
            }
            messages.success(request,f"برای شماره همراه{form.cleaned_data['phone']} کد تایید ارسال گردید",'success')
            return redirect('accounts:accounts-verify')
        return render(request,self.template_class,{'form':form})
        
            
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