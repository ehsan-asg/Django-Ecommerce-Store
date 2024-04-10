from django.urls import path,include
from . import views
from django.views.decorators.cache import cache_page


app_name = "accounts"

urlpatterns = [
    # path('',include('django.contrib.auth.urls'))
    path('login/',views.LoginView.as_view(),name="login"),
    path('verify/',views.OTPVerificationView.as_view(),name="verify"),
    path('register/',views.UserRegistrationView.as_view(),name="register"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
]
