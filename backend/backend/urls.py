from django.contrib import admin
from django.urls import path, include, re_path
from django_prometheus import exports


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('rest.urls')),
    path("metrics/", exports.ExportToDjangoView)
]