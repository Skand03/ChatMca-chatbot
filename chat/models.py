from django.db import models

class Message(models.Model):
    """
    Represents a single chat message in the conversation.
    """
    user_message = models.TextField()
    assistant_reply = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"User: {self.user_message[:50]} | Assistant: {self.assistant_reply[:50]}"
