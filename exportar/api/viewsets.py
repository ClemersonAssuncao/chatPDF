from rest_framework import viewsets
from chatbot.api import serializers
from chatbot import models


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MessageSerializer
    queryset = models.Message.objects.all()
    http_method_names= ['get', 'post']
    