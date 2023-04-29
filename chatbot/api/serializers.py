from rest_framework import serializers
from chatbot import models

class MessageSerializer(serializers.ModelSerializer):
    class Meta:        
        model = models.Message
        fields = '__all__'
