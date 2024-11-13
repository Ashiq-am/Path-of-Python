#models.py
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', null=True)
    bio = models.TextField(blank=True, default= 'This is a default bio')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
