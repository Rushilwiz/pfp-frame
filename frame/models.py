from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from django.core.files import File
from PIL import Image
import requests
from io import BytesIO
from urllib.request import urlretrieve


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.get_full_name()}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if bool(self.image):
            img = Image.open(self.image.path)
            frame = Image.open(settings.MEDIA_ROOT + "/frame.png")
            img.thumbnail((500, 500))
            width, height = img.size
            frame.thumbnail((width, height))
            img.paste(frame, (0,0), frame)
            img.save(self.image.path)