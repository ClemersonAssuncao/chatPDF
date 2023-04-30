from rest_framework.views import APIView
from .serializers import MessageSerializer
from rest_framework.response import Response
from chatbot import models
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework import status

class chatBotApiView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        books = models.Message.objects.all()
        serializer = MessageSerializer(books, many=True)
        return Response(serializer.data)
    
    @csrf_exempt
    def post(self, request):
        serializer = models.Message(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)