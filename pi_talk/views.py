from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from profiles.models import UserProfile

def administrator(request):
    # if the user is authenticated if not send them to a log in page

    return render(request, 'pi_talk/index.html', )


def index(request):

    context = {
        'title': "Login",

    }
    if request.user.is_authenticated:
        context['title'] = "Pi Talk"


    return render(request, 'pi_talk/index.html',context)
