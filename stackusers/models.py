from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250, default="Software Developer")
    image = models.ImageField(default="raccoon.png", upload_to="profilepics")
    phone = models.IntegerField(default=123456789)

    def __str__(self):
        return f"{self.user.username} - Profile"