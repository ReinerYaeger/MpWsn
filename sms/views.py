from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from profiles.models import UserProfile
from .models import LocationSoilSensorData


# from sms.forms import SignupForm
# from django.contrib.gis.geos import Point


def index(requests):
    context = {
        'title': "Home",

    }
    return render(requests, 'sms/index.html',context)


def experiment(requests):
    context = {

    }
    return render(requests, 'sms/experiment.html',context)


def live_analytics(requests):
    context = {
        'title': "Live Data Analysis",

    }
    return render(requests, 'sms/technique/live_analytics.html', context)


def experiment_results(requests):
    context = {
        'title': "Results",

    }
    return render(requests, 'sms/technique/live_analytics.html', context)


def sensor_dataset(requests):
    dataset = serialize('geojson', LocationSoilSensorData.objects.all())

    return HttpResponse(dataset, content_type='json')


def map_view(requests, parish=None):
    context = {
        'title': "Map of Jamaica Live Analysis",
        "sensor_data": serialize('geojson', LocationSoilSensorData.objects.all()),
        'settings_overrides': {
            'DEFAULT_CENTER': (17.9279, -76.7162),
            'SPATIAL_EXTENT': (-76.4016, 17.8564, -76.2925, 17.9926),
            'DEFAULT_ZOOM': 15,
            'MAX_ZOOM': 20,
            'MIN_ZOOM': 15,
        }
    }

    if parish is not None:
        print(1)

    return render(requests, 'sms/map/jamaica.html', context)

def administrator(request):

    return render(request, 'pi_talk/index.html', {'user_profile': user_profiles})