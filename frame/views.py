from django.shortcuts import render
from django.conf import settings
from allauth.socialaccount.models import SocialToken

from .models import Profile

from urllib.request import urlretrieve
from django.core.files import File

import requests

# Create your views here.

def login(request):
    return render(request, 'frame/login.html')

def redirect(request):
    if not Profile.objects.filter(user=request.user).exists():
        profile = Profile(user=request.user)
        profile.save()
        req = urlretrieve(profile.user.socialaccount_set.first().get_avatar_url())
        profile.image.save("image.jpg", File(open(req[0], 'rb')))
    else:
        profile = Profile.objects.get(user=request.user)
 
    return render(request, 'frame/redirect.html', context={'data': profile})