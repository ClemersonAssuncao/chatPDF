from django.urls import path
from . import views
# from .api.viewApi import chatBotApiView

urlpatterns = [
    path('chatBot/executeMessage/', views.executeMessage),
    path('', views.index, name='index'),
    #path('message/', views.executeMessage, name='message'),
]