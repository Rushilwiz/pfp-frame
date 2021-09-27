from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from PIL import Image
import requests
from io import BytesIO


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.get_full_name()}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        r = requests.get(self.user.socialaccount_set.first().get_avatar_url())
        img = Image.open(BytesIO(r.content))
        img.thumbnail((300,300))
        print(img)
        print(settings.MEDIA_ROOT + self.image.name)
        self.image.save("image.jpg", img)