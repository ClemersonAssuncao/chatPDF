from rest_framework.views import APIView
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from chatbot import models
from django.conf import settings
import openai

class chatBotApiView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request):
        books = models.Message.objects.all()
        serializer = MessageSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):

        session_key = request.session.session_key
        
        if (session_key):
            conversation, created = models.Conversation.objects.get_or_create(session_key=session_key, user= request.user)
            message = models.Message(text=request.POST['text'], user = request.user, conversation=conversation)
            message.save()
            conversation.messages.add(message)

        openai.api_key = settings.OPEN_AI_API_KEY
        response = openai.Completion.create(
            engine="davinci",
            prompt=request.POST['text'],
            stop=['\nHuman'],
            temperature=0,
            n=1,
            frequency_penalty=0,
            presence_penalty=0,
            best_of=1,
        )
        print(response.choices)
        return Response(response.choices[0].text)