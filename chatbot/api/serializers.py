from rest_framework import serializers
from chatbot import models

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:        
        model = models.Conversation
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:        
        model = models.Message
        fields = '__all__'
