from rest_framework import viewsets
from menu.models import OrderList, Restaurant
from rest.serializers.core import OrderListSerializer, OrderListCreateSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from menu.controllers.order_list_controller import *

# ViewSet для меню
class OrderListViewSet(viewsets.ModelViewSet):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer
    http_method_names = ['get', 'post', 'delete']
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
  
    def destroy(self, request, pk=None):
        if request.user.is_staff:
            orderList = get_object_or_404(OrderList, pk=pk)
            OrderController().delete(orderList)
            return Response("ok", status=204)
        else:
            return Response("Пользователь не авторизован", status=205)