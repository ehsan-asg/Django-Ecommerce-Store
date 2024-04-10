from django.contrib.auth import views as auth_views
from django.views.generic.edit import FormView
from accounts.forms import AuthenticationForm,SignupForm,VerifyCodeForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.views import View
from .models import OtpCode
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
import random

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True




class UserRegistrationView(FormView):
    template_name = 'accounts/register.html'
    form_class = SignupForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']

        otp_code = random.randint(1000, 9999)
        OtpCode.objects.create(email=form.cleaned_data['email'], code=otp_code)
        self.request.session['otp_code'] = otp_code
        self.request.session['email'] = email
        self.request.session['password'] = password

        return redirect('accounts:verify')



class OTPVerificationView(View):
    template_name = 'accounts/verify.html'
    form_class = VerifyCodeForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        otp_code = request.POST.get('code')
        expected_otp_code = str(request.session.get('otp_code', ''))
        email = request.session.get('email')
        password = request.session.get('password')

        if otp_code == expected_otp_code:
            user = get_user_model().objects.create_user(email=email, password=password)
            user.is_active = True
            user.is_verified = True
            user.save()

            user = authenticate(username=email, password=password)
            login(request, user)
            OtpCode.objects.get(code=otp_code).delete()
            return redirect('website:index')
        else:
            messages.error(request, 'کد وارد شده نادرست است.')
            return render(request, self.template_name, {'form': self.form_class})


class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True      
class LogoutView(auth_views.LogoutView):
    pass

