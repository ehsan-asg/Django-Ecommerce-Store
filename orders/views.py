from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import AddressSerializers,CouponSerializers,OrderSerializers,OrderItemSerializers
from .models import Address,Coupon,Order,OrderItem
from product.models import Feature
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.utils import timezone
import json


#template
class ShoppingTemplateView(TemplateView):
    template_name = 'shopping.html'
class PayTemplateView(TemplateView):
      template_name = "shopping-peyment.html"
class ShoppingCompleteBuyTemplateView(TemplateView):
      template_name = "shopping-complete-buy.html"
class ShoppingCompleteNotBuyTemplateView(TemplateView):
      template_name = "shopping-no-complete-buy.html"
#api
class AddressDetailApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = get_object_or_404(get_user_model(), phone_number=request.user.phone_number)
        addresses = Address.objects.filter(user=user,deleted=False)
        serializer = AddressSerializers(addresses, many=True)
        return Response(serializer.data)

class AddressCreateApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = AddressSerializers(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AddressDeleteApiView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        address = Address.objects.get(pk=pk)
        address.delete()
        return Response({'message': 'Address deleted'}, status=status.HTTP_200_OK)
class CouponCheckApiView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, code):
        try:
            coupon = Coupon.objects.get(code=code)
            now = timezone.now()
            valid_from = coupon.valid_from
            valid_to = coupon.valid_to
            code = coupon.code
            discount = coupon.discount
            if valid_from <= now <= valid_to:
                return Response({"message": "Coupon is active","coupon":code,"discount":discount})
            else:
                return Response({"message": "Coupon is not active","coupon":code,"discount":discount}, status=status.HTTP_400_BAD_REQUEST)
        except Coupon.DoesNotExist:
            return Response({"error": "Coupon not found"}, status=status.HTTP_404_NOT_FOUND)

class OrderCreateApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user = get_user_model().objects.get(id=request.user.id)
            discount = request.data['discount']
            
            list_order = json.loads(request.data['list-order'])

            order = Order.objects.create(user=user, discount=discount)
            
            for cart in list_order:
                product_id = cart['id']
                feature = Feature.objects.get(id=cart['feature_data'])  
                price = cart['first_price']
                quantity = cart['quantity']

                OrderItem.objects.create(order=order, product_id=product_id, Feature=feature, price=price, quantity=quantity)

            return Response({"message": "The order was successfully placed"},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# class OrderListApiView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         try:
#           user = get_user_model().objects.get(id=request.user.id)

#         except Exception as e:
#             return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    