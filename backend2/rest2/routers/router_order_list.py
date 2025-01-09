from rest_framework import routers

from rest2.viewsets.orderlist import OrderListViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'order_list', OrderListViewSet, basename='order_list')