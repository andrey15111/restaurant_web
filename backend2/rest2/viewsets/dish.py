from rest_framework import viewsets
from core.models import Dish
from rest2.serializers import DishSerializer, CreateDish, UpdateDish
from rest_framework.response import Response
from rest_framework import viewsets
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from core.controllers.dish_controller import *
from django.shortcuts import get_object_or_404

# ViewSet для меню
class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    http_method_names = ['get']
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