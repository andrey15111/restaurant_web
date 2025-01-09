from django.conf.urls import include
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest.routers.router_auth import router as router_auth
from rest.routers.router_menu import router as router_menu
from rest.routers.router_order import router as router_order
from rest.routers.router_order_list import router as router_order_list
from rest.routers.router_dish import router as router_dish

schema_view = get_schema_view(
    openapi.Info(
        title="ADMIN",
        default_version='v1',
        description="API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("auth/", include(router_auth.urls)),
    path("menu/", include(router_menu.urls)),
    path("order/", include(router_order.urls)),
    path("order_list/", include(router_order_list.urls)),
    path("dish/", include(router_dish.urls))
]