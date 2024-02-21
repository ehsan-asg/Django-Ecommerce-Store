from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

app_name = 'shop'
urlpatterns = [
  path("",views.HomeView.as_view(),name="home"),
  path("product-category/<slug:category_slug>/",views.CategoryView.as_view(),name="product-category"),
  path("product/<slug:product_slug>/",views.SingleProductView.as_view(),name="single-product"),
  #API
  path("api/HomeProductView/",views.HomeProductView.as_view()),
  path("api/product-category/<slug:category_slug>/",views.CategoryApiView.as_view()),
  path("api/product/<slug:product_slug>/",views.SingleProductApiView.as_view())
]
