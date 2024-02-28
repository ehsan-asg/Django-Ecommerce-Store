from django.urls import path
from . import views
app_name="orders"
urlpatterns = [
    path("shopping/",views.ShoppingTemplateView.as_view(),name="shopping-template"),
    #api 
    path("api/address/create/",views.AddressCreateApiView.as_view()),
    path("api/address/detail/",views.AddressDetailApiView.as_view()),
    path("api/address/delete/<int:pk>/",views.AddressDeleteApiView.as_view())
]