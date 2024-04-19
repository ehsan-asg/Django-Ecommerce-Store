from typing import Any
from django.shortcuts import render
from django.views.generic import  TemplateView
from .cart import CartSession
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CartItemSerializer
from rest_framework import status

class CartSummaryView(TemplateView):
    template_name = "cart/cart-summary.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        cart = CartSession(self.request.session)
        cart_items = cart.get_cart_items()
        context["cart_items"] = cart_items
        context["total_quantity"] = cart.get_total_quantity()
        context["total_payment_price"] = cart.get_total_payment_amount()
        return context
class AddCartApiview(APIView):
      def post(self,request):
          ser_data = CartItemSerializer(data=request.POST,context={'request': request})
          if ser_data.is_valid():
              ser_data.create(ser_data.validated_data)
              return Response(ser_data.data, status=status.HTTP_201_CREATED)
          return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
class RemoveProductView(APIView):
      def post(self,request):
          ser_data = CartItemSerializer(data=request.POST,context={'request': request})
          if ser_data.is_valid():
             ser_data.delete(ser_data.validated_data)
             return Response(ser_data.data,status=status.HTTP_201_CREATED)
          return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
class changeProductView(APIView):
      def post(self,request):
          ser_data = CartItemSerializer(data=request.POST,context={'request': request})
          if ser_data.is_valid():
             ser_data.updateproduct_Method(ser_data.validated_data)
             return Response(ser_data.data,status=status.HTTP_201_CREATED)
          return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

