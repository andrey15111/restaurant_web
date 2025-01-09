from rest_framework import routers

from rest.viewsets.auth import AuthViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'simple', AuthViewSet, basename='simple')