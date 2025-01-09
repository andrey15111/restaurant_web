from rest_framework import serializers
from core.models import AuthModel, Menu, Order, Dish, OrderList

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthModel
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CreateDish(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField()
    menu = serializers.IntegerField()

class UpdateDish(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField()

class CreateMenu(serializers.Serializer):
    name = serializers.CharField()
    restaurant = serializers.IntegerField()

class UpdateMenu(serializers.Serializer):
    name = serializers.CharField()

class DishItemSerializer(serializers.Serializer):
    dish_id = serializers.IntegerField()
    count = serializers.IntegerField()
    price = serializers.FloatField()


class OrderListSerializer(serializers.ModelSerializer):
    dishes = DishItemSerializer(many=True)
    class Meta:
        model = OrderList
        fields = '__all__'

class OrderListCreateSerializer(serializers.Serializer):
    dishes = DishItemSerializer(many=True)
    restaurant = serializers.IntegerField()



class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
