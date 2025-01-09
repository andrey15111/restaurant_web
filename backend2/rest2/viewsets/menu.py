from rest_framework import viewsets
from core.models import Menu, Order, Restaurant
from rest2.serializers import MenuSerializer, CreateMenu, UpdateMenu
from rest_framework.response import Response
from rest_framework import viewsets
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
# ViewSet для меню

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    http_method_names = ['get']

    @swagger_auto_schema(
        operation_description="Получение списках всех блюд",
        responses={
            200: "Успешно",
            404: "Не удалось получить файл"
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, args, kwargs)