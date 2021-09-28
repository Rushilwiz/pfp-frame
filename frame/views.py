from django.shortcuts import render
from django.conf import settings

from .models import Profile

from urllib.request import urlretrieve
from django.core.files import File

# Create your views here.

def login(request):
    return render(request, 'frame/login.html')

def redirect(request):
    if not Profile.objects.filter(user=request.user).exists():
        profile = Profile(user=request.user)
        profile.save()
        req = urlretrieve(profile.user.socialaccount_set.first().get_avatar_url())
        profile.image.save("image.jpg", File(open(req[0], 'rb')))

    return render(request, 'frame/redirect.html', context={'data': profile})