from django.contrib.auth import views as auth_views
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.edit import FormView
from accounts.forms import AuthenticationForm,SignupForm,VerifyCodeForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib import messages
from django.core.cache import cache
from utils import send_otp_email
from django.conf import settings
import redis
import random

# Redis
redis_client = redis.Redis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True

class UserRegistrationView(FormView):
    template_name = 'accounts/register.html'
    form_class = SignupForm
    

    def dispatch(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect("website:index")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']

        otp_code = random.randint(1000, 9999)
        redis_client.setex(form.cleaned_data['email'], 180, otp_code)
        send_otp_email(form.cleaned_data['email'], otp_code)
        self.request.session["user_verify"] = {
                "otp_code": otp_code,
                "email":email,
                "password":password
         }

        return redirect('accounts:verify')



class OTPVerificationView(View):
    template_name = 'accounts/verify.html'
    form_class = VerifyCodeForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("website:index")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data['code']
            user_verify = request.session.get('user_verify')
            expected_otp_code = user_verify['otp_code']
            email = user_verify['email']
            password = user_verify['password']

            if otp_code == expected_otp_code:
                print("test")
                user = get_user_model().objects.create_user(email=email, password=password)
                user.is_active = True
                user.is_verified = True
                user.save()
                user = authenticate(username=email, password=password)
                login(request, user)
                request.session['user_verify'].clear()
                return redirect('website:index')
            else:
                messages.error(request, 'کد وارد شده نادرست است.')
        return render(request, self.template_name, {'form': form})


class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True     
class LogoutView(auth_views.LogoutView):
    pass



