from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Conversation(models.Model):
    session_key = models.CharField(max_length=255)
    user = models.ForeignKey(User, db_column="user", on_delete= models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)

class Message (models.Model):
    
    user = models.ForeignKey(User, db_column="user", on_delete= models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        db_table = 'Message'
