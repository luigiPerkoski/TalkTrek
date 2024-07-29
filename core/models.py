from django.db import models
from django.contrib.auth.models import AbstractUser

class CoreUser(AbstractUser):
    friends = models.ManyToManyField('self', blank=True, related_name='friends')
    bio = models.TextField(blank=True, null=True)
    online_status = models.BooleanField(default=False)

    def __str__(self):
        return f' {self.username} || {self.email}'


class Message(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('received', 'Received'),
        ('read', 'Read'),
    ]

    id = models.AutoField(primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='sent') 
    user = models.ForeignKey(CoreUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.texto[:50]} - {self.status}'


class Room(models.Model):
    friends = models.ManyToManyField(CoreUser, related_name='rooms')
    user = models.ForeignKey(CoreUser, related_name='created_rooms', on_delete=models.CASCADE)
    message_list = models.ManyToManyField(Message, blank=True)


