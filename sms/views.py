import logging
import threading

from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import SensorCollectedData, SensorGroup, SensorGroupManager
from django.views.decorators.csrf import csrf_exempt
from .forms import ChartDataForm


def index(requests):
    context = {
        'title': "Home",

    }
    return render(requests, 'sms/index.html', context)


def experiment(requests):
    context = {

    }
    return render(requests, 'sms/experiment.html', context)


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
    dataset = serialize('geojson', SensorGroup.objects.all())

    return HttpResponse(dataset, content_type='json')


def map_view(requests, parish=None):
    context = {
        'title': "Map of Jamaica Live Analysis",
        "sensor_data": serialize('geojson', SensorCollectedData.objects.all()),
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
    return render(request, 'pi_talk/index.html', )


@login_required(login_url=index)
def data_manager(request):
    return render(request, 'sms/data_handler.html')


def chart_data(request):

    return render(request, 'your_template.html', )
