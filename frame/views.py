from django.shortcuts import render
from django.conf import settings

from .models import Profile

# Create your views here.

def login(request):
    return render(request, 'frame/login.html')

def redirect(request):
    if not Profile.objects.filter(user=request.user).exists():
        profile = Profile(user=request.user)
        profile.save()
    else:
        profile = Profile.objects.get(user=request.user)
        profile.delete()
        profile = Profile(user=request.user)
        profile.save()
    return render(request, 'frame/redirect.html', context={'data': profile})