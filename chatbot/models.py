from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message (models.Model):
    
    user = models.ForeignKey(User, db_column="user", on_delete= models.CASCADE)
    date = models.DateField()
    text = models.TextField()

    class Meta:
        db_table = 'Message'
