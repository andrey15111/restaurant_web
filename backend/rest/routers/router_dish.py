from rest_framework import routers

from rest.viewsets.dish import DishViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'dish', DishViewSet, basename='dish')