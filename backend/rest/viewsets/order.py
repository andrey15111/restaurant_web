from rest_framework import viewsets
from menu.models import AuthModel, Menu, Order
from rest.serializers.core import OrderSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from menu.controllers.order_list_controller import *
from django.shortcuts import get_object_or_404

# ViewSet для заказов
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'delete', 'post']
    permission_classes = [IsAuthenticated]

    def destroy(self, request, pk=None):
        if request.user.is_staff:
            dish = get_object_or_404(Order, pk=pk)
            OrderController().delete(dish)
            return Response("ok", status=204)
        else:
            return Response("Пользователь не авторизован", status=205)