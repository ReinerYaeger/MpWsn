from django.shortcuts import render
from iot.pi_files import arduino_interface
from iot.pi_files import server
from threading import Thread

# Create your views here.


def index(requests):

    context = {}

    return render(requests, 'sms/index.html', context)
