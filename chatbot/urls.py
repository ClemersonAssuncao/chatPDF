from django.urls import path
from . import views
from .api.chatBotApiView import chatBotApiView

urlpatterns = [
    path('api/chat/', chatBotApiView.as_view(), name='chat'),
    path('', views.index, name='index'),
    #path('message/', views.executeMessage, name='message'),
]