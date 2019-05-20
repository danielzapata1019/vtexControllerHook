from django.contrib import admin
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    url("api/v1/", include("orders.urls")),
    url("admin/", admin.site.urls)
]