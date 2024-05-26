
from rest_framework import serializers
from .models import User, Product, Car, Order, ProductSee, ProductLike, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'phone_number', 'date_created', 'date_update', 'is_active', 'is_admin']

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ProductSeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductSee
        fields = '__all__'

class ProductLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLike

class CarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Car
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    