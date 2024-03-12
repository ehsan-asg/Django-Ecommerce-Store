from django.urls import path
from . import views
app_name="orders"
urlpatterns = [
    path("shopping/",views.ShoppingTemplateView.as_view(),name="shopping-template"),
    path("shopping/pay/",views.PayTemplateView.as_view(),name="shopping-pay-template"),
    path('shopping/complete-order/',views.ShoppingCompleteBuyTemplateView.as_view(),name="shopping-complete-buy-template"),
    path('shopping/not-complete-order/',views.ShoppingCompleteNotBuyTemplateView.as_view(),name="shopping-not-complete-buy-template"),
    #api 
    path("api/address/create/",views.AddressCreateApiView.as_view()),
    path("api/address/detail/",views.AddressDetailApiView.as_view()),
    path("api/address/delete/<int:pk>/",views.AddressDeleteApiView.as_view()),
    path('api/coupon/check/<slug:code>/',views.CouponCheckApiView.as_view()),
    path('api/order/',views.OrderCreateApiView.as_view())
]