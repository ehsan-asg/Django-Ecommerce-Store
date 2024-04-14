from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class AuthenticationForm(auth_forms.AuthenticationForm):
    def confirm_login_allowed(self, user):
        super(AuthenticationForm,self).confirm_login_allowed(user)


class SignupForm(forms.Form):
    input_class = ' form-control form-control-lg text-center'
    input_id = "signupSimpleLoginPassword"
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': input_class,"id":input_id}),label='ایمیل')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': input_class,"id":input_id}),label='کلمه عبور')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': input_class,"id":input_id}),label='تکرار کلمه عبور')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user = get_user_model().objects.filter(email=email).exists()
        if user:
            raise forms.ValidationError('این ایمیل از قبل موجود است')
        return email
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('رمزهای ورود مطابقت ندارند')
        return cd['password2']


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg text-center'}),label="کد تایید")

    
    