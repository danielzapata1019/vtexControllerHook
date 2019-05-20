from django.conf.urls import url, include
from orders import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url('obtenerpedidos', views.obtenerPedidos, name='obtenerPedidos'),
]

urlpatterns = format_suffix_patterns(urlpatterns)