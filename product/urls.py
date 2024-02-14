from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
  path("",views.HomeView.as_view(),name="home"),
  #API
  path("api/HomeProductView/",views.HomeProductView.as_view())
]
