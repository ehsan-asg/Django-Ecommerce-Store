from rest_framework import serializers
from shop.models import ProductModel, ProductStatusType
from .cart import CartSession
from django.http import JsonResponse

class CartItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate(self, data):
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        if not product_id:
            raise serializers.ValidationError("Product ID is required.")

        if not quantity:
            raise serializers.ValidationError("Quantity is required.")
        try:
            product = ProductModel.objects.get(id=product_id, status=ProductStatusType.publish.value)
        except ProductModel.DoesNotExist:
            raise serializers.ValidationError("Product does not exist or is not published")
        
        if product.stock < quantity:
           raise serializers.ValidationError("The quantity requested exceeds the quantity in stock")
        return data

    def create(self, validated_data):
        product_id = validated_data.get('product_id')
        request = self.context.get('request')
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        if product_id and ProductModel.objects.filter(id=product_id, status=ProductStatusType.publish.value).exists():

            cart.add_product(product_id)
        if request.user.is_authenticated:
            cart.merge_session_cart_in_db(request.user)
        return JsonResponse({"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity()})


    def delete(self, instance):
        request = self.context.get('request')
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        if product_id:
            cart.remove_product(product_id)
        if request.user.is_authenticated:
            cart.merge_session_cart_in_db(request.user)
        return JsonResponse({"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity()})
        
    def updateproduct_Method(self, validated_data):
        request = self.context.get('request')
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")
        if product_id and quantity:
            cart.update_product_quantity(product_id, quantity)
        if request.user.is_authenticated:
            cart.merge_session_cart_in_db(request.user)
        return JsonResponse({"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity()})





