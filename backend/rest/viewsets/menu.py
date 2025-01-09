from rest_framework import viewsets
from menu.models import Menu, Order, Restaurant
from rest.serializers.core import MenuSerializer, CreateMenu, UpdateMenu
from rest_framework.response import Response
from rest_framework import viewsets
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from menu.controllers.menu_controller import *
from menu.controllers.mail_sender import *
from django.shortcuts import get_object_or_404
# ViewSet для меню

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
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
        request_body = CreateMenu,
        responses={
            200: "Успешно",
            205: "Пользователь не имеет доступа"
        }
    )
    def create(self, request):
        controller = MenuController()
        name = request.data["name"]
        restaurant = get_object_or_404(Restaurant, id=request.data["restaurant"])
        if request.user.is_staff:
            controller = MenuController().create(name, restaurant)
            serializer = MenuSerializer(controller)
            return Response(serializer.data, status=200)
        else:
            return Response("Пользователь не авторизован", status=205)

    @swagger_auto_schema(
        operation_description="Получение списках всех блюд",
        request_body = UpdateMenu,
        responses={
            200: "Успешно",
            205: "Пользователь не имеет доступа"
        }
    )
    def partial_update(self, request, pk=None, *args, **kwargs):
        if request.user.is_staff:
            controller = MenuController(pk)
            name = request.data["name"]
            serializer = MenuSerializer(controller.edit(name))
            return Response(serializer.data, status=201)
        else:
            return Response("Пользователь не авторизован", status=205)
            
    def destroy(self, request, pk=None):
        if request.user.is_staff:
            dish = get_object_or_404(Menu, pk=pk)
            MenuController().delete(dish)
            return Response("ok", status=204)
        else:
            return Response("Пользователь не авторизован", status=205)