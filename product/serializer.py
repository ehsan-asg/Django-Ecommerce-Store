from rest_framework import serializers
from .models import Product,Category,Feature,Discount


class ProductSerializers(serializers.ModelSerializer):
    feature = serializers.SerializerMethodField()
    Category = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = "__all__"
    def get_feature(self, obj):
        result = obj.feature.all()
        return FeatureSerializers(instance=result, many=True).data
    def get_Category(self, obj):
        result = obj.Category.all()
        return CategorySerializers(instance=result, many=True).data
class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class FeatureSerializers(serializers.ModelSerializer):
      class Meta:
        model = Feature
        fields = "__all__"
class DiscountSerializers(serializers.ModelSerializer):
      class Meta:
          model = Discount
          fields = "__all__"