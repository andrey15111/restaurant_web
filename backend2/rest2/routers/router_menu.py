from rest_framework import routers

from rest2.viewsets.menu import MenuViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'menu', MenuViewSet, basename='menu')