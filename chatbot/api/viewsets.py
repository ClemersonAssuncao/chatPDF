from rest_framework import viewsets
from chatbot.api import serializers
from chatbot import models
from .serializers import MessageSerializer
from rest_framework.response import Response
from chatbot import models
from rest_framework import status


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MessageSerializer
    queryset = models.Message.objects.all()
    http_method_names= ['get', 'post']
    
    def get(self, request, format=None):
        print('asd')
        drinks = models.Message.objects.all()
        serializer = MessageSerializer(drinks, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        print('asd')
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)