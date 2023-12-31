from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def administrator(request, username):
	# if the user is authenticated if not send them to a log in page
	user_profiles = get_object_or_404(UserProfile, user__username=username)
	return render(request, 'profile/user_profile.html', {'user_profile': user_profiles})


def index(request):
	return render(request, 'profiles/index.html')
