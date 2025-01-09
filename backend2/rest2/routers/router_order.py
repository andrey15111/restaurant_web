from rest_framework import routers

from rest2.viewsets.order import OrderViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'order', OrderViewSet, basename='order')