from rest_framework.views import APIView
from .serializers import MessageSerializer
from rest_framework.response import Response
from chatbot import models
from rest_framework import status

class chatBotApiView(APIView):
    
    def get(self, request, format=None):
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