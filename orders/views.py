from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import AddressSerializers
from .models import Address
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

#template
class ShoppingTemplateView(TemplateView):
    template_name = 'shopping.html'
#api
class AddressDetailApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = get_object_or_404(get_user_model(), phone_number=request.user.phone_number)
        addresses = Address.objects.filter(user=user)
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