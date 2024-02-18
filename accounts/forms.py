from typing import Any
from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'


    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="you can change password using <a href=\"../password/\">this form</a>.")
    class Meta:
        model = User
        fields = ('phone_number','email','full_name','password','last_login')

class UserRegisterForm(forms.Form):
    phone = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class': "input-ui pr-2",'placeholder': 'شماره موبایل خود را وارد نمایید'}))
    full_name = forms.CharField(label='full name',widget=forms.TextInput(attrs={'class': "input-ui pr-2",'placeholder': 'نام و نام خانوادگی خود را وارد نمایید'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "input-ui pr-2",'placeholder': 'رمز عبور خود را وارد نمایید'}))

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = User.objects.filter(phone_number=phone).exists()
        if user:
            raise ValidationError('this phone number already exist')
        elif not phone.isdigit():
            raise ValidationError("Phone number can only contains digits")
        elif len(phone) !=11:
            raise ValidationError('Length of phone number must be 11 digits')
        return phone
    
class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()

class LoginForm(forms.Form):
    phone = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class': "input-ui pr-2",'placeholder': 'شماره موبایل خود را وارد نمایید'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "input-ui pr-2",'placeholder': 'رمز عبور خود را وارد نمایید'}))

