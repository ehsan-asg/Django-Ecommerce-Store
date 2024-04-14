from django.urls import path,re_path
from . import views

app_name = "cart"

urlpatterns = [
    path("summary/",views.CartSummaryView.as_view(),name="cart-summary"),
    path("api/add-cart/",views.AddCartApiview.as_view(),name="add-cart-item"),
    path("api/remover-cart/",views.RemoveProductView.as_view(),name="remove-cart-item"),
    path("api/change-product-quantity/",views.changeProductView.as_view(),name="change-quantity-product")
]

