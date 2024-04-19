from rest_framework import serializers
from .models import ProductModel

class ProductSerializers(serializers.ModelSerializer):
      class Meta:
            model = ProductModel
            fields = ["title","slug","price","image"]
      