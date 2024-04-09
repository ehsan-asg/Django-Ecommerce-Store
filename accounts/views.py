from django.contrib.auth import views as auth_views
from django.views.generic.edit import FormView
from accounts.forms import AuthenticationForm,SetPasswordForm
from accounts.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.views import View
from .forms import UserRegistrationForm
import random

class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Generate OTP
            otp_code = random.randint(100000, 999999)

            # Save user but don't activate yet
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = False
            user.save()

            # Send OTP to user via email
            send_mail(
                'Your OTP Code',
                f'Your OTP code is: {otp_code}',
                'from@example.com',
                [email],
                fail_silently=False,
            )

            # Redirect to OTP verification page
            return redirect('otp_verification', username=username)

        return render(request, 'registration/register.html', {'form': form})

class OTPVerificationView(View):
    def get(self, request, username):
        return render(request, 'registration/otp_verification.html', {'username': username})

    def post(self, request, username):
        otp_code = request.POST.get('otp_code')
        if otp_code:
            # Check if OTP is correct
            if otp_code == request.session.get('otp_code'):
                # Activate user
                user = User.objects.get(username=username)
                user.is_active = True
                user.save()

                # Log the user in
                user = authenticate(username=username)
                login(request, user)

                return redirect('home')  # Redirect to home page after successful login

        return render(request, 'registration/otp_verification.html', {'username': username})

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True      
class LogoutView(auth_views.LogoutView):
    pass