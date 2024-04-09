from typing import Mapping
from django.contrib.auth import forms as auth_forms
from django.core.exceptions import ValidationError
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList



class AuthenticationForm(auth_forms.AuthenticationForm):
    def confirm_login_allowed(self, user):
        super(AuthenticationForm,self).confirm_login_allowed(user)

# class SetPasswordForm(forms.Form):
#     error_messages = {
#         'password_mismatch': _("The two password fields didn't match."),
#     }
#     username = forms.EmailField(_("email address"), unique=True)
#     is_staff = forms.BooleanField(default=False)
#     is_active = forms.BooleanField(default=True)
#     is_verified = forms.BooleanField(default=False)
#     new_password1 = forms.CharField(label=_("New password"),
#                                     widget=forms.PasswordInput)
#     new_password2 = forms.CharField(label=_("New password confirmation"),
#                                     widget=forms.PasswordInput)
#     def __init__(self, user,*args,**kwargs):
#         self.user = user
#         super(SetPasswordForm,self).__init__(*args,**kwargs)

#     def clean_new_password2(self):
#         password1 = self.cleaned_data.get('new_password1')
#         password2 = self.cleaned_data.get('new_password2')
#         if password1 and password2:
#             if password1 != password2:
#                 raise forms.ValidationError(
#                     self.error_messages['password_mismatch'],
#                     code='password_mismatch',
#                 )
#             return password2
#     def save(self):
#         pass