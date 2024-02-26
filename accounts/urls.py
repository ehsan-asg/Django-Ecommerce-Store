from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
app_name = 'accounts'
urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name="accounts-register-template"),
    path('verify/',views.UserVerifyCodeView.as_view(),name="accounts-verify-template"),
    path('login/',views.UserLoginCodeView.as_view(),name="accounts-login-template"),
    path('address/create/',views.UserAddAddress.as_view(),name="accounts-add-address"),
    path("profile/",views.UserProfileTemplateView.as_view(),name="accounts-profile-template"),
    #api 
    path('api/register/', views.UserRegister.as_view(), name='user-register'),
    path('api/verify-code/', views.UserVerifyCode.as_view(), name='user-verify-code'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user',views.UserAllView.as_view(),name="accounts-user"),
]
