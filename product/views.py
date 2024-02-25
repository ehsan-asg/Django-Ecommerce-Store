from django.shortcuts import render,get_object_or_404,get_list_or_404
from rest_framework import generics
from rest_framework.response import Response
from django.views import View
from .models import Product,Category
from .serializer import ProductSerializers,CategorySerializers
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.utils.encoding import uri_to_iri

class HomeView(View):
    def get(self,request):
        return render(request,"landing-page/index.html")

class CategoryView(View):
      def get(self,request,category_slug):
          return render(request,"shop/product-category.html")

class SingleProductView(View):
     def get(self,request,product_slug):
          return render(request,"shop/single-product.html")

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

class CategoryApiView(APIView,PageNumberPagination):
      page_size = 3
      def get(self,request,category_slug):
           product_category = get_object_or_404(Category, slug=category_slug)
           products = product_category.products.all()
           pagination_products = self.paginate_queryset(products,request,view=self)
           ser_data = ProductSerializers(pagination_products,many=True).data
           count = products.count()
           return Response({'count': count, 'results': ser_data},status=status.HTTP_200_OK)
class SingleProductApiView(APIView):
     def get(self,request,product_slug):
          product_query = get_object_or_404(Product,slug=product_slug)
          ser_data = ProductSerializers(product_query).data
          return Response(ser_data,status=status.HTTP_200_OK)
class CartTemplateView(TemplateView):
     template_name = "shop/cart.html"