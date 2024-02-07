from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('register/',views.RegisterUserView.as_view(),name="accounts-register"),
    path('verify/',views.UserRegisterVerifyCodeView.as_view(),name="accounts-verify")
]
