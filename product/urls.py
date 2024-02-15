from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
  path("",views.HomeView.as_view(),name="home"),
  path("product-category/<slug:category_slug>/",views.CategoryView.as_view(),name="product-category"),
  #API
  path("api/HomeProductView/",views.HomeProductView.as_view()),
  path("api/product-category/<slug:category_slug>/",views.CategoryApiView.as_view())
]
