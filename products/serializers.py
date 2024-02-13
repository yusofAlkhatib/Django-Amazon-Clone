
from rest_framework import serializers
from .models import Product , Brand , Review , ProductImages

class BrandListSerialzer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    class Meta:
        model = Brand
        fields = '__all__'

    def get_products_count(self,object):
        count = object.product_brand.all().count()
        return count

         


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields ='__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    product_image = ProductImagesSerializer(many=True)
    review_product = ReviewSerializer(many=True)
    
    class Meta:
        model = Product
        fields ='__all__'


class BrandDetailSerialzer(serializers.ModelSerializer):
    product_brand = ProductListSerializer(many=True)
    products_count = serializers.SerializerMethodField()
    class Meta:
        model = Brand
        fields = '__all__'


    def get_products_count(self,object):
        count = object.product_brand.all().count()
        return count
    
    
    