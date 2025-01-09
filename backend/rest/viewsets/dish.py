from rest_framework import viewsets
from menu.models import Dish
from rest.serializers.core import DishSerializer, CreateDish, UpdateDish
from rest_framework.response import Response
from rest_framework import viewsets
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from menu.controllers.dish_controller import *
from django.shortcuts import get_object_or_404

# ViewSet для меню
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Получение списках всех блюд",
        responses={
            200: "Успешно",
            404: "Не удалось получить файл"
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, args, kwargs)
    
    @swagger_auto_schema(
        operation_description="Получение списках всех блюд",
        request_body = CreateDish,
        responses={
            200: "Успешно",
            205: "Пользователь не имеет доступа"
        }
    )
    def create(self, request):
        controller = DishController()
        name = request.data["name"]
        price = request.data["price"]
        menu = get_object_or_404(Menu, id=request.data["menu"])
        if request.user.is_staff:
            controller = DishController().create(name, price, menu)
            serializer = DishSerializer(controller)
            return Response(serializer.data, status=200)
        else:
            return Response("Пользователь не авторизован", status=205)

    @swagger_auto_schema(
        operation_description="Получение списках всех блюд",
        request_body = UpdateDish,
        responses={
            200: "Успешно",
            205: "Пользователь не имеет доступа"
        }
    )
    def partial_update(self, request, pk=None, *args, **kwargs):
        if request.user.is_staff:
            controller = DishController(pk)
            name = request.data["name"]
            price = request.data["price"]
            serializer = DishSerializer( controller.edit(name, price))
            return Response(serializer.data, status=201)
        else:
            return Response("Пользователь не авторизован", status=205)
            
    def destroy(self, request, pk=None):
        if request.user.is_staff:
            dish = get_object_or_404(Dish, pk=pk)
            DishController().delete(dish)
            return Response("ok", status=204)
        else:
            return Response("Пользователь не авторизован", status=205)