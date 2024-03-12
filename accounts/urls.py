from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
app_name = 'accounts'
urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name="accounts-register-template"),
    path('verify/',views.UserVerifyCodeView.as_view(),name="accounts-verify-template"),
    path('login/',views.UserLoginCodeView.as_view(),name="accounts-login-template"),
    path('logout/',views.UserLogoutView.as_view(),name="accounts-logout"),
    path('address/create/',views.UserAddAddress.as_view(),name="accounts-add-address"),
    path("profile/",views.UserProfileTemplateView.as_view(),name="accounts-profile-template"),
    path("profile/address/",views.UserProfileAddressView.as_view(),name="accounts-profile-address"),
    path("profile/order/",views.UserProfileOrder.as_view(),name="accounts-profile-order"),
    #api 
    path('api/register/', views.UserRegister.as_view(), name='user-register'),
    path('api/verify-code/', views.UserVerifyCode.as_view(), name='user-verify-code'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/userall',views.UserAllView.as_view(),name="accounts-user"),
    path("api/user",views.UserDetailView.as_view(),name="user-details")
]
