

from .models import Person, Product, Login, Category
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from .serializers import PersonSerializer, LoginSerializer, ProductSerializer, CategorySerializer, SellerSerializer, Seller_ProductSerializer, OrderSerializer, CartSerializer, AbcSerializer
from rest_framework.response import Response




class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [permissions.IsAuthenticated]
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []
class SellerViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = SellerSerializer
    permission_classes = []
class Seller_ProductViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = Seller_ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
class CartViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
'''
class AbcView(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = AbcSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        queryset = Category.objects.all()
        serializer = AbcSerializer(queryset, many=True)
        return Response(serializer.data)

'''