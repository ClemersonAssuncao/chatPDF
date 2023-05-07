from django.urls import path
from .api.exportarApiView import exportarApiView
from . import views

urlpatterns = [
    path('api/enviar-arquivo/', exportarApiView.as_view(), name='enviar-arquivo')
]