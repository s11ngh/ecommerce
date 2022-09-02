from .models import Person, Product, Cart, Seller, Order, Category, Seller_Product, Login
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name']

        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'product_id', 'discount', 'category_id']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['seller_id']
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product_id', 'seller_id']
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product_id']
class Seller_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller_Product
        fields = ['name']
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['user_id']
        
class AbcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
