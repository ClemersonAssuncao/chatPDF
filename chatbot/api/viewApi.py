from rest_framework.views import APIView
from .serializers import MessageSerializer
from rest_framework.response import Response
from chatbot import models
from rest_framework import status

class viewApi(APIView):
    
    def post(self, request):
        print("Minha mensagem de teste")
        return Response({"mensagem": "Mensagem enviada com sucesso"})