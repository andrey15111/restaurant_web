from rest_framework import viewsets
from core.models import AuthModel, Menu, Order
from rest2.serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from core.controllers.order_list_controllers import *
from django.shortcuts import get_object_or_404

# ViewSet для заказов
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def list(self, request):
        orders = Order.objects.filter(username=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)