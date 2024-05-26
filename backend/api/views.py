from django.shortcuts import render
from rest_framework import generics
from .models import User, Product, Comment, ProductSee, ProductLike, Order, Car
from .serializers import UserSerializer, ProductSerializer, CommentSerializer, ProductSeeSerializer, ProductLikeSerializer, OrderSerializer, CarSerializer

# User database views
class UserListCreateApi(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Product
class ProductListCreateApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CommentListCreateApi(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# User Register Products
class ProductSeeListCreateApi(generics.ListCreateAPIView):
    queryset = ProductSee.objects.all()
    serializer_class = ProductSeeSerializer

class ProductSeeRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductSee.objects.all()
    serializer_class = ProductSeeSerializer

class ProductLikeListCreateApi(generics.ListCreateAPIView):
    queryset = ProductLike.objects.all()
    serializer_class = ProductLikeSerializer

class ProductLikeRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductLike.objects.all()
    serializer_class = ProductLikeSerializer

# Orders by users in the front
class OrderListCreateApi(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CarListCreateApi(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarRetrieveUpdateDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer