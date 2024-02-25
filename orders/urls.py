from django.urls import path
from . import views
app_name="orders"
urlpatterns = [
    #api 
    path("api/address/create",views.AddressCreateApiView.as_view())
]