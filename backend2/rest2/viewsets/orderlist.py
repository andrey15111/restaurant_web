from rest_framework import viewsets
from core.models import OrderList, Restaurant
from rest2.serializers import OrderListSerializer, OrderListCreateSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from core.controllers.order_list_controllers import *

# ViewSet для меню
class OrderListViewSet(viewsets.ModelViewSet):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer
    http_method_names = ['post']
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Получение списках всех блюд",
        request_body = OrderListCreateSerializer,
        responses={
            200: "Успешно",
            205: "Пользователь не имеет доступа"
        }
    )
    def create(self, request):
        restaurant = get_object_or_404(Restaurant, id=request.data["restaurant"])
        controller = OrderController().create(request.user, request.data['dishes'], request.data['restaurant'])
        serializer = OrderListSerializer(controller)
        return Response(serializer.data, status=200)
