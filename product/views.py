from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from django.views import View
from .models import Product,Category
from .serializer import ProductSerializers,CategorySerializers
from rest_framework import status,pagination
from rest_framework.views import APIView

class HomeView(View):
    def get(self,request):
        return render(request,"landing-page/index.html")


class HomeProductView(APIView):
    def get(self, request):
        laptop_category = get_object_or_404(Category, slug='category-notebook-netbook-ultrabook')
        mobile_category = get_object_or_404(Category, slug='mobile')
        mouse_category = get_object_or_404(Category,slug="category-mouse")

        
        laptop_products = laptop_category.products.all()
        mobile_products = mobile_category.products.all()
        mouse_products =  mouse_category.products.all()
        laptop_serializer = ProductSerializers(laptop_products, many=True).data
        mobile_serializer = ProductSerializers(mobile_products, many=True).data
        mouse_serializer = ProductSerializers(mouse_products, many=True).data

        response_data = {
                "laptop_products": laptop_serializer,
                "mobile_products": mobile_serializer,
                "mouse_products": mouse_serializer
        }

        return Response(response_data, status=status.HTTP_200_OK)